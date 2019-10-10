"""
Custom JSON Schema resolver
"""
import colorama
import io
import json
import os
import re
import sys

from jsonschema import RefResolver
from jsonschema.compat import urldefrag
from typing import Any

dynamic_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "dynamic_cases"))


def check_profiles_skip(*profiles: str) -> bool:
    profiles = list(map(str.lower, profiles))
    profiles_orig = os.getenv("testProfiles", "").split(",")
    profiles_lower = list(map(str.lower, profiles_orig))

    if len({*profiles} - {*profiles_lower}) == 0:
        matches = list(map(profiles_orig.pop, list(map(profiles_lower.index, profiles))))
        os.environ["testProfiles"] = ",".join(profiles_orig)
        return False
    return True


def safe_load(msg_file) -> dict:
    with open(msg_file, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return {}


def load_cases(profile: str, case: str) -> list:
    cases = []
    case_path = os.path.join(dynamic_dir, profile.lower(), case)
    if os.path.isdir(case_path):
        cases = [(
            os.path.splitext(f)[0],
            safe_load(os.path.join(case_path, f))
        ) for f in os.listdir(case_path) if f.endswith(".json")]
    return cases


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
        tmp = self.colorize(f"\n{txt}", "UNDERLINE", "BOLD", "FG_CYAN")
        print(tmp)

    def h2(self, txt):
        print(self.colorize(f"\n{txt}", "UNDERLINE", "BOLD", "FG_WHITE"))

    def debug(self, txt):
        print(self.colorize(txt, "FG_WHITE"))

    def info(self, txt):
        print(self.colorize(f"> {txt}",  "FG_WHITE"))

    def success(self, txt):
        print(self.colorize(txt, "FG_GREEN"))

    def error(self, txt):
        print(self.colorize(f"x {txt}", "FG_RED"))

    def warn(self, txt):
        print(self.colorize(f"-> {txt}", "FG_YELLOW"))

    def bold(self, txt):
        print(self.colorize(txt, "BOLD"))

    def note(self, txt):
        print(f"{self.colorize('Note:', 'UNDERLINE', 'BOLD', 'FG_CYAN')} {self.colorize(txt, 'FG_CYAN')}")

    def default(self, txt):
        txt = self._toStr(txt)
        print(self.colorize(txt))

    def verbose(self, style, txt):
        if style is not "verbose" and hasattr(self, style) and callable(getattr(self, style)):
            if self._verbose:
                getattr(self, style)(txt)
            else:
                self._log(txt)
