"""
Simple Testing of OpenC2 Command & Responses
"""
import os
import unittest

from argparse import Namespace
from datetime import datetime
from use_cases import create_test_suite, test_setup, utils

# Exit on first fail/error or show all fails/errors after all tests
exitOnFail = False

profiles = [
    # Add profiles to test here
    "Language",
    "Extension",
    "General",
    "SLPF",
]

file_dir = os.path.dirname(os.path.realpath(__file__))
log_dir = os.path.join(file_dir, "logs")
schema_dir = os.path.join(file_dir, "schemas")

schemas = dict(
    # SCHEMA_NAME=(SCHEMA_FILE, COMMAND_RECORD, RESPONSE_RECORD),
    # oc2ls_wd14=(f"{schema_dir}/oc2ls-v1.0-wd14.json", "openc2_command", "openc2_response"),
    oc2ls_wd14_update=f"{schema_dir}/oc2ls-v1.0-wd14_update.json",
    # romano=f"{schema_dir}/romanojd/message.json",
    # bberliner=f"{schema_dir}/bberliner/combined_schema.json",
    bberliner_gen=(f"{schema_dir}/oc2ls-v1.0.1-bb_gen.json", "openc2_command", "openc2_response"),
    # dkemp=f"{schema_dir}/oc2ls-v1.0-csprd03_dk.json",
    lang_gen=(f"{schema_dir}/oc2ls-v1.1-lang_gen.json", "openc2_command", "openc2_response"),
    # slpf_gen=(f"{schema_dir}/oc2slpf-v1.0-refs_gen.json", "openc2_command", "openc2_response"),
)


def default_namespace(v) -> Namespace:
    data = {
        "file": f"{schema_dir}/oc2ls-v1.0-wd14_update.json",
        "command": "OpenC2-Command",
        "response": "OpenC2-Response"
    }
    data.update(dict(zip(data.keys(), (v, ) if isinstance(v, str) else v)))
    return Namespace(**data)


def format_result(pre: str, count: int, total: int) -> str:
    percent = f"{(count/total)*100:.2f}%"
    return f"{pre} {count:,}/{total:,} ({percent}) tests"


if __name__ == "__main__":
    os.environ["testProfiles"] = ",".join(profiles)
    now = datetime.now()
    # console = utils.ConsoleStyle(True, f"{log_dir}/schema_tests_{now:%Y.%m.%d_%H.%M.%S}.log")
    console = utils.ConsoleStyle()

    console.h1(f"Testing OpenC2 Schema - {now:%Y %B %d}")
    console.h2(f"Testing Profiles: {', '.join(profiles)}")
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)

    ignore = ["errors", "skipped", ]

    for name, info in schemas.items():
        console.h2(f"Running unittests against {name} schema, logfile -> ./logs/{name}.log")
        info = default_namespace(info)
        test_setup.SetupTests.schema_file = info.file
        test_setup.SetupTests.root_dir = os.path.dirname(info.file)
        test_setup.SetupTests.cmd_exp = info.command  # Override for Command record name
        test_setup.SetupTests.rsp_exp = info.response  # Override for Response record name

        with open(f"{log_dir}/{name}.log", "w") as test_log:
            testSuite = create_test_suite()
            profile_tests = os.getenv("unknownProfiles", "")
            if profile_tests:
                console.warn(f"Unknown profile tests specified: {', '.join(profile_tests.split(','))}")

            tests = unittest.TextTestRunner(stream=test_log, failfast=exitOnFail).run(testSuite)
            testsRun = tests.testsRun-len(tests.skipped)

            console.info(format_result("Ran", tests.testsRun-len(tests.skipped), tests.testsRun))
            console.warn(format_result("Skipped", len(tests.skipped), tests.testsRun))
            console.error(format_result("Error", len(tests.errors), testsRun))
            console.error(format_result("Failure", len(tests.failures), testsRun))
            passed = testsRun - ( + len(tests.failures) + len(tests.errors))
            console.success(format_result("Passed", passed, testsRun))
