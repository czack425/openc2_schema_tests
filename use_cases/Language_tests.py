"""
OpenC2 Language Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "Language"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} tests not specified")
class Language_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
