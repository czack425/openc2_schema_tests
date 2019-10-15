"""
OpenC2 U. of Oslo: Stateful Packet Filtering Custom Profile Use Case Command/Response Pairs Template
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "X_SFPF"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class X_SFPF_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile
    # good_commands = load_cases(profile, "commands-good")
    # bad_commands = load_cases(profile, "commands-bad")
    # good_responses = load_cases(profile, "response-good")
    # bad_responses = load_cases(profile, "response-bad")

    # Static Validation Functions
