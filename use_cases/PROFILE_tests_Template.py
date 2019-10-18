"""
OpenC2 Profile Use Case Command/Response Pairs Template
Edit the profile variable for the specific profile being created, and add custom tests if desired
Dynamic test messages will be loaded from `use_cases/dynamic_cases/PROFILE/` with four sub folders
- good-commands -> Good Commands, should not raise an error
- bad-commands -> Bad Commands, should raise an error
- good-responses -> Good Responses, should not raise an error
- bad-responses -> Bad Responses, should raise an error
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

    # Static Validation Functions
