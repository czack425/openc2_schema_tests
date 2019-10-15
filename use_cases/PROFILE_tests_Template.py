"""
OpenC2 Profile Use Case Command/Response Pairs Template
Edit the profile variable for the specific profile being created, and add custom tests if desired
Dynamic test messages will be loaded from `use_cases/dynamic_cases/PROFILE/` with four sub folders
- commands_good -> Good Commands, should not raise an error
- commands_bad -> Bad Commands, should raise an error
- responses_good -> Good Responses, should not raise an error
- responses_bad -> Bad Responses, should raise an error
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "PROFILE"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class PROFILE_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile
    # good_commands = load_cases(profile, "commands-good")
    # bad_commands = load_cases(profile, "commands-bad")
    # good_responses = load_cases(profile, "response-good")
    # bad_responses = load_cases(profile, "response-bad")

    # Static Validation Functions
