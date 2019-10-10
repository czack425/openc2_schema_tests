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

# GitHub API Token for extra test cases from Brian Berliner - https://github.com/bberliner/openc2-json-schema
# os.environ["GitHubToken"] = ...

os.environ["testProfiles"] = ",".join([
    # Add profiles to test here
    "Language",
    "Extension",
    "General",
    "SLPF",
    "SFPF",
    "Route",
    "X_ICDX",
    "X_SEPM",
    "X_FAM",
    "X_EGAS",
    # "X_SFPF",
    # "X_Route",
])

file_dir = os.path.dirname(os.path.realpath(__file__))
log_dir = os.path.join(file_dir, "logs")
schema_dir = os.path.join(file_dir, "schemas")

schemas = dict(
    # SCHEMA_NAME=(SCHEMA_FILE, COMMAND_RECORD, RESPONSE_RECORD),
    oc2ls_wd14=(f"{schema_dir}/oc2ls-v1.0-wd14.json", "openc2_command", "openc2_response"),
    oc2ls_wd14_reorg=f"{schema_dir}/oc2ls-v1.0-wd14_reorg.json",
    oc2ls_wd14_update=f"{schema_dir}/oc2ls-v1.0-wd14_update.json",
    romano=f"{schema_dir}/romanojd/message.json",
    bberliner=f"{schema_dir}/bberliner/combined_schema.json",
    dkemp=f"{schema_dir}/oc2ls-v1.0-csprd03_dk.json",
    lang_gen=f"{schema_dir}/oc2ls-v1.1-lang_gen.json",
    # slpf_gen=f"{schema_dir}/oc2slpf-v1.0-refs_gen.json",
)


def default_namespace(v) -> Namespace:
    data = {
        "file": f"{schema_dir}/oc2ls-v1.0-wd14_update.json",
        "command": "OpenC2-Command",
        "response": "OpenC2-Response"
    }
    data.update(dict(zip(data.keys(), (v, ) if isinstance(v, str) else v)))
    return Namespace(**data)


if __name__ == "__main__":
    now = datetime.now()
    # console = utils.ConsoleStyle(True, f"{log_dir}/schema_tests_{now:%Y.%m.%d_%H.%M.%S}.log")
    console = utils.ConsoleStyle()

    console.h1(f"Testing OpenC2 Schema - {now:%Y %B %d}")
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)

    for name, info in schemas.items():
        console.h2(f"Running unittests against {name} schema, logfile -> ./logs/{name}.log")
        info = default_namespace(info)
        test_setup.SetupTests.schema_file = info.file
        test_setup.SetupTests.root_dir = os.path.dirname(info.file)
        test_setup.SetupTests.cmd_exp = info.command  # Override for Command record name
        test_setup.SetupTests.rsp_exp = info.response  # Override for Response record name

        with open(f"{log_dir}/{name}.log", "w") as test_log:
            testSuite = create_test_suite()
            profile_tests = os.getenv("testProfiles", "")
            if profile_tests:
                console.warn(f"Unknown profile tests specified: {', '.join(profile_tests.split(','))}")

            unittest.TextTestRunner(stream=test_log, failfast=exitOnFail).run(testSuite)
