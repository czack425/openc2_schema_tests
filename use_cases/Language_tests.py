"""
OpenC2 Language Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from parameterized import parameterized
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "Language"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} tests not specified")
class Language_UseCases(SetupTests):
    good_commands = load_cases(profile, "commands-good")
    bad_commands = load_cases(profile, "commands-bad")
    good_responses = load_cases(profile, "response-good")
    bad_responses = load_cases(profile, "response-bad")

    # Dynamic Validation Functions
    @unittest.skipIf(good_commands == [], f"{profile}: no good command test cases")
    @parameterized.expand(load_cases(profile, "commands-good"), skip_on_empty=True)
    def test_good_commands(self, name, msg):
        self.validate(msg, self.cmd_exp)

    @unittest.skipIf(bad_commands == [], f"{profile}: no bad command test cases")
    @parameterized.expand(load_cases(profile, "commands-bad"), skip_on_empty=True)
    def test_bad_commands(self, name, msg):
        with self.assertRaises(ValidationError):
            self.validate(msg, self.cmd_exp)

    @unittest.skipIf(good_responses == [], f"{profile}: no good response test cases")
    @parameterized.expand(load_cases(profile, "response-good"), skip_on_empty=True)
    def test_good_response(self, name, msg):
        self.validate(msg, self.cmd_exp)

    @unittest.skipIf(bad_responses == [], f"{profile}: no bad response test cases")
    @parameterized.expand(load_cases(profile, "response-bad"), skip_on_empty=True)
    def test_bad_response(self, name, msg):
        with self.assertRaises(ValidationError):
            self.validate(msg, self.cmd_exp)

    # Static Validation Functions
