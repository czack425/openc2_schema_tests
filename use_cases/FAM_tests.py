"""
OpenC2 Trend Micro: File Anti-malware Custom Profile (FAM) Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "X_FAM"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class FAM_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile
    # good_commands = load_cases(profile, "commands-good")
    # bad_commands = load_cases(profile, "commands-bad")
    # good_responses = load_cases(profile, "response-good")
    # bad_responses = load_cases(profile, "response-bad")

    # Static Validation Functions
