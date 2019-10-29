"""
Custom JSON Schema resolver
"""
import colorama
import copy
import io
import json
import os
import re
import sys
import unittest

from jsonschema import RefResolver
from jsonschema.compat import urldefrag
from typing import (
    Any,
    Callable,
    Dict
)

dynamic_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "dynamic_cases"))


def check_profiles_skip(*profiles: str) -> bool:
    profiles = list(map(str.lower, profiles))
    profiles_orig = os.getenv("TestProfiles", "").split(",")
    profiles_unknown = os.environ.setdefault("unknownProfiles", ",".join(profiles_orig)).split(",")
    profiles_lower = list(map(str.lower, profiles_orig))

    if len({*profiles} - {*profiles_lower}) == 0:
        matches = list(map(profiles_orig.pop, list(map(profiles_lower.index, profiles))))
        os.environ["unknownProfiles"] = ",".join([p for p in profiles_unknown if p not in matches])
        return False
    return True


def clean_var_name(var: str) -> str:
    # Remove invalid characters
    var = re.sub('[^0-9a-zA-Z_]', '', var)
    # Remove leading characters until a letter or underscore
    var = re.sub('^[^a-zA-Z_]+', '', var)
    return var


def load_cases(profile: str) -> Dict[str, Any]:
    version = os.getenv("LangVersion", "v1.0")
    profile = profile.lower()
    cases = ("good-commands", "bad-responses", "bad-commands", "good-responses")
    dynamic_cases = {}

    if not os.path.isdir(os.path.join(dynamic_dir, version)):
        raise NotADirectoryError(f"Language version {version} does not have tests defined")

    for case in cases:
        case_path = os.path.join(dynamic_dir, version, profile, case)
        case = case.replace("-", "_")
        if os.path.isdir(case_path):
            dynamic_cases[case] = {}
            for f in os.listdir(case_path):
                if f.endswith(".json"):
                    dynamic_cases[case][os.path.splitext(f)[0]] = safe_load(os.path.join(case_path, f))

    return dynamic_cases


def safe_load(msg_file) -> dict:
    with open(msg_file, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return {}


def short_exception(fun: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            raise e.__class__(getattr(e, "message", str(e)))
    return wrapper


class ExtendedResolver(RefResolver):
    def __init__(self, base_uri, referrer, store=(), cache_remote=True, handlers=(), urljoin_cache=None, remote_cache=None, root_dir=None):
        super(ExtendedResolver, self).__init__(base_uri, referrer, store, cache_remote, handlers, urljoin_cache, remote_cache)
        self.root_scope = self._scopes_stack[0]
        self.root_dir = root_dir

    def resolve_from_url(self, url):
        uri, ref = urldefrag(url)

        try:
            doc = self.store[uri]
        except KeyError:
            doc = self.resolve_remote(uri) if not re.search(self.root_scope, uri) else super().resolve_from_url(url)

        return self.resolve_fragment(doc, ref)

    def resolve_remote(self, uri):
        doc = None

        if not doc:
            doc = self.resolve_file(uri)

        if not doc:
            doc = super().resolve_remote(uri)

        return doc

    def resolve_file(self, uri):
        """
        resolve a schema path
        :param uri: path appended to root
        :return: resolved schema
        :return: resolved schema
        """
        path, file = self._get_uri_scope(uri)
        doc = None

        if self.root_dir and os.path.isdir(self.root_dir):
            schema_path = os.path.join(self.root_dir, file)
            if os.path.isfile(schema_path):
                with open(schema_path, "r") as f:
                    doc = json.load(f)

        if doc and self.cache_remote:
            self.store[uri] = doc

        return doc if doc else {}

    # Helper Functions
    def _get_uri_scope(self, uri):
        """
        Split the URI into the path and file
        :param uri: uri to get the scope
        :return: tuple - path - file
        """
        uri, ref = uri.split("#", 1) if "#" in uri else (uri, "")
        uri = uri.split("/")
        return "/".join(uri[:-1]), uri[-1]


class ObjectDict(dict):
    """
    Dictionary that acts like a object
    d = ObjectDict()

    d['key'] = 'value'
        SAME AS
    d.key = 'value'
    """

    def __getattr__(self, key: Any) -> Any:
        """
        Get an key as if an attribute - ObjectDict.key - SAME AS - ObjectDict['key']
        :param key: key to get value of
        :return: value of given key
        """
        if key in self:
            return self[key]
        else:
            raise AttributeError(f"No such attribute {key}")

    def __setattr__(self, key: Any, val: Any) -> None:
        """
        Set an key as if an attribute - d.key = 'value' - SAME AS - d['key'] = 'value'
        :param key: key to create/override
        :param val: value to set
        :return: None
        """
        self[key] = self.__class__(val) if isinstance(val, dict) else val

    def __delattr__(self, key: Any) -> None:
        """
        Remove a key as if an attribute - del d.key - SAME AS - del d['key']
        :param key: key to remove/delete
        :return: None
        """
        if key in self:
            del self[key]
        else:
            raise AttributeError(f"No such attribute: {key}")


class FrozenDict(ObjectDict):
    """
    Immutable/Frozen dictionary
    """

    def __hash__(self) -> int:
        """
        Create a hash for the FrozenDict
        :return: object hash
        """
        if self._hash is None:
            self._hash = hash(tuple(sorted(self.items())))
        return self._hash

    def _immutable(self, *args, **kwargs) -> None:
        """
        Raise an error for an attempt to alter the FrozenDict
        :param args: positional args
        :param kwargs: key/value args
        :return: None
        :raise TypeError
        """
        raise TypeError('cannot change object - object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    pop = _immutable
    popitem = _immutable
    clear = _immutable
    update = _immutable
    setdefault = _immutable


class SchemaTestResults(unittest.TextTestResult):
    _testReport = {}

    def getTestsReport(self, raw: bool = False) -> Dict[str, Dict[str, Any]]:
        """
        Returns the run tests as a list of the form of a dict
        """
        rtn = copy.deepcopy(self._testReport)

        for p in rtn:
            rtn[p]["total"] = len({f for t in rtn[p].values() for f in t})

            if not raw:
                for t in rtn[p]:
                    if t in ("error", "failure"):
                        rtn[p][t] = {k: rtn[p][t][k] for k in {*rtn[p][t].keys()} - {*rtn[p].get("success", {}).keys()}}

        rtn["stats"] = dict(
            total=sum([rtn[p].get("total", 0) for p in rtn]),
            error=sum([len(rtn[p].get("error", {})) for p in rtn]),
            failure=sum([len(rtn[p].get("failure", {})) for p in rtn]),
            skipped=sum([len(rtn[p].get("skipped", {})) for p in rtn]),
            expected_failure=sum([len(rtn[p].get("expected_failure", {})) for p in rtn]),
            unexpected_success=sum([len(rtn[p].get("unexpected_success", {})) for p in rtn]),
        )

        def toFrozen(d: Any):
            r = d
            if isinstance(d, dict):
                return FrozenDict({k: toFrozen(v) for k, v in d.items()})

            if isinstance(d, (list, tuple)):
                return tuple(FrozenDict(i) for i in d)

            return r

        return toFrozen(rtn)

    def addError(self, test: unittest.case.TestCase, err) -> None:
        super().addError(test, err)
        profile = getattr(test, "profile", "Unknown")
        self._addReport(profile, "error", test)

    def addFailure(self, test: unittest.case.TestCase, err) -> None:
        super().addFailure(test, err)
        profile = getattr(test, "profile", "Unknown")
        self._addReport(profile, "failure", test)

    def addSuccess(self, test: unittest.case.TestCase) -> None:
        super().addSuccess(test)
        profile = getattr(test, "profile", "Unknown")
        self._addReport(profile, "success", test)

    def addExpectedFailure(self, test: unittest.case.TestCase, err) -> None:
        super().addExpectedFailure(test, err)
        profile = getattr(test, "profile", "Unknown")
        self._addReport(profile, "expected_failure", test)

    def addSkip(self, test: unittest.case.TestCase, reason: str) -> None:
        super().addSkip(test, reason)
        profile = getattr(test, "profile", "Unknown")
        self._addReport(profile, "skipped", test)

    def addUnexpectedSuccess(self, test: unittest.case.TestCase) -> None:
        super().addUnexpectedSuccess(test)
        profile = getattr(test, "profile", "Unknown")
        self._addReport(profile, "unexpected_success", test)

    # Helper Functions
    def _addReport(self, profile: str, category: str, test: unittest.case.TestCase) -> None:
        self._testReport.setdefault(profile, {}).setdefault(category, {})[test._testMethodName] = test


class ConsoleStyle:
    def __init__(self, verbose=False, log=None):
        colorama.init()
        self._verbose = verbose if isinstance(verbose, bool) else False

        self._logFile = None
        if self._verbose and isinstance(log, (str, io.TextIOWrapper)):
            self._logFile = log

        self._encoding = sys.getdefaultencoding()
        self._format_regex = re.compile(r"\[\d+m", flags=re.MULTILINE)
        self._textStyles = FrozenDict({
            # Styles
            "RESET": colorama.Fore.RESET,
            "NORMAL": colorama.Style.NORMAL,
            "DIM": colorama.Style.DIM,
            "BRIGHT": colorama.Style.BRIGHT,
            # Text Colors
            "FG_BLACK": colorama.Fore.BLACK,
            "FG_BLUE": colorama.Fore.BLUE,
            "FG_CYAN": colorama.Fore.CYAN,
            "FG_GREEN": colorama.Fore.GREEN,
            "FG_MAGENTA": colorama.Fore.MAGENTA,
            "FG_RED": colorama.Fore.RED,
            "FG_WHITE": colorama.Fore.WHITE,
            "FG_YELLOW": colorama.Fore.YELLOW,
            "FG_RESET": colorama.Fore.RESET,
            # Background Colors
            "BG_BLACK": colorama.Back.BLACK,
            "BG_BLUE": colorama.Back.BLUE,
            "BG_CYAN": colorama.Back.CYAN,
            "BG_GREEN": colorama.Back.GREEN,
            "BG_MAGENTA": colorama.Back.MAGENTA,
            "BG_RED": colorama.Back.RED,
            "BG_WHITE": colorama.Back.WHITE,
            "BG_YELLOW": colorama.Back.YELLOW,
            "BG_RESET": colorama.Back.RESET,
        })

    def _toStr(self, txt):
        return txt.decode(self._encoding, "backslashreplace") if hasattr(txt, "decode") else txt

    def colorize(self, txt, *styles):
        txt = self._toStr(txt)
        self._log(txt)
        color_text = "".join([self._textStyles.get(s.upper(), "") for s in styles]) + txt
        return f"\033[0m{color_text}\033[0m"

    def _log(self, txt):
        if self._logFile:
            if isinstance(self._logFile, str):
                with open(self._logFile, 'a+') as f:
                    f.write(f"{self._format_regex.sub('', self._toStr(txt))}\n")
            elif isinstance(self._logFile, io.TextIOWrapper):
                self._logFile.write(f"{self._format_regex.sub('', self._toStr(txt))}\n")

    def underline(self, txt):
        print(self.colorize(txt, "UNDERLINE", "BOLD"))

    def h1(self, txt):
        print(self.colorize(f"\n{txt}", "UNDERLINE", "BOLD", "FG_CYAN"))

    def h2(self, txt):
        print(self.colorize(f"\n{txt}", "UNDERLINE", "BOLD", "FG_WHITE"))

    def h3(self, txt):
        print(self.colorize(f"\n{txt}", "UNDERLINE", "BOLD", "FG_MAGENTA"))

    def debug(self, txt):
        print(self.colorize(txt, "FG_WHITE"))

    def info(self, txt):
        print(self.colorize(f"* {txt}",  "FG_WHITE"))

    def success(self, txt):
        print(self.colorize(f"+ {txt}", "FG_GREEN"))

    def error(self, txt):
        print(self.colorize(f"x {txt}", "FG_RED"))

    def warn(self, txt):
        print(self.colorize(f"> {txt}", "FG_YELLOW"))

    def bold(self, txt):
        print(self.colorize(txt, "BOLD"))

    def note(self, txt):
        print(f"{self.colorize('Note:', 'UNDERLINE', 'BOLD', 'FG_CYAN')} {self.colorize(txt, 'FG_CYAN')}")

    def default(self, txt):
        print(self.colorize(txt))

    def verbose(self, style, txt):
        if style is not "verbose" and hasattr(self, style) and callable(getattr(self, style)):
            if self._verbose:
                getattr(self, style)(txt)
            else:
                self._log(txt)
