"""
Simple Testing of OpenC2 Command & Responses
"""
import os
import unittest

from argparse import Namespace
from datetime import datetime
from use_cases import create_test_suite, test_setup, utils

# Verbose - Show test breakdown by profile
verbose = False

# Exit on first fail/error or show all fails/errors after all tests
exitOnFail = False

# Versions to test, should be prefixed as v...
version = "v1.0"

# Add profiles to test here
profiles = [
    # "Language",
    # "Extension",
    # "General",
    # "SLPF",
    # "SLPF-Acme",
    # Non Profile Specific
    "BBerliner"
]

file_dir = os.path.dirname(os.path.realpath(__file__))
log_dir = os.path.join(file_dir, "logs")
schema_dir = os.path.join(file_dir, "schemas")


schemas = dict(
    # SCHEMA_NAME=(SCHEMA_FILE, COMMAND_RECORD, RESPONSE_RECORD),
    # oc2ls_wd14=(f"{schema_dir}/oc2ls-v1.0-wd14.json", "openc2_command", "openc2_response"),
    oc2ls_v1_0=f"{schema_dir}/oc2ls-v1.0.1_hii.json",
    # oc2ls_v1_1_update=f"{schema_dir}/oc2ls-v1.1-wd14_update.json",
    # romano=f"{schema_dir}/romanojd/message.json",
    # bberliner=f"{schema_dir}/bberliner/combined_schema.json",
    bberliner_gen=(f"{schema_dir}/oc2ls-v1.0.1-bb_gen.json", "openc2_command", "openc2_response"),
    # dkemp=f"{schema_dir}/oc2ls-v1.0-csprd03_dk.json",
    lang_gen=(f"{schema_dir}/oc2ls-v1.0.1_gen.json", "openc2_command", "openc2_response"),
    # Profile Schemas
    # oc2slpf_v1_0=f"{schema_dir}/oc2slpf-v1.0.json",
    # slpf_gen=(f"{schema_dir}/oc2slpf-v1.0-refs_gen.json", "openc2_command", "openc2_response"),
)

tests_format = (
    ("warn", "Skipped"),
    ("error", "Error"),
    ("error", "Failure"),
    ("success", "Success"),
    # ("error", "Expected_Failure"),
    # ("warn", "Unexpected_Success")
)


def default_namespace(v) -> Namespace:
    data = {
        "file": f"{schema_dir}/oc2ls-v1.0-wd14_update.json",
        "command": "OpenC2-Command",
        "response": "OpenC2-Response"
    }
    data.update(dict(zip(data.keys(), v if isinstance(v, tuple) else (v, ))))
    return Namespace(**data)


def format_result(pre: str, count: int, total: int) -> str:
    percent = f"{(count/total)*100:.2f}%" if total > 0 else f"{0:.2f}%"
    return f"{pre} {count:,}/{total:,} ({percent}) tests"


if __name__ == "__main__":
    console = utils.ConsoleStyle(verbose=verbose)
    os.environ["LangVersion"] = version
    os.environ["TestProfiles"] = ",".join(profiles)

    now = datetime.now()
    console.h1(f"Testing OpenC2 Schema - {now:%Y %B %d}")
    console.info(f"Testing Profiles: {', '.join(profiles)}")
    console.info(f"Using tests for {version}")
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)

    for name, info in schemas.items():
        console.h2(f"Running unittests against {name} schema, logfile -> ./logs/{name}.log")
        info = default_namespace(info)
        test_setup.SetupTests.schema_file = info.file
        test_setup.SetupTests.root_dir = os.path.dirname(info.file) if isinstance(info.file, str) else schema_dir
        test_setup.SetupTests.cmd_exp = info.command  # Override for Command record name
        test_setup.SetupTests.rsp_exp = info.response  # Override for Response record name

        with open(f"{log_dir}/{name}.log", "w") as test_log:
            testSuite = create_test_suite()
            profile_tests = os.getenv("unknownProfiles", "")
            if profile_tests:
                console.warn(f"Unknown profile tests specified: {', '.join(profile_tests.split(','))}")

            results = unittest.TextTestRunner(
                stream=test_log,
                failfast=exitOnFail,
                resultclass=utils.SchemaTestResults
            ).run(testSuite)
            breakdown = results.getTestsReport()
            stats = breakdown.stats
            testsRun = stats.total - stats.skipped

            console.info(format_result("Ran", testsRun, stats.total))
            console.warn(format_result("Skipped", stats.skipped, stats.total))
            console.error(format_result("Error", stats.error, testsRun))
            console.error(format_result("Failure", stats.failure, testsRun))
            passed = testsRun - (stats.failure + stats.error)
            console.success(format_result("Passed", passed, testsRun))

            for profile in ({*breakdown.keys()} - {"stats"}):
                tests = breakdown[profile]
                console.verbose("h3", format_result(f"{profile} ->", tests.total, testsRun))
                for fun, msg in tests_format:
                    console.verbose(fun, format_result(msg, len(tests.get(msg.lower(), {})), tests.total))
            console.verbose("default", "")
