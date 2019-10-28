"""
OpenC2 Language Use Case Command/Response Pairs
"""
import unittest

from .test_setup import SetupTests, ValidationError
from .utils import check_profiles_skip

profile = "Language"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} tests not specified")
class Language_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
