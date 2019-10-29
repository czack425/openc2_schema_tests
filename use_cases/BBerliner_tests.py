"""
OpenC2 Profile Use Case Command/Response Pairs from Brian Berliner
"""
import unittest

from .test_setup import SetupTests, ValidationError
from .utils import check_profiles_skip

profile = "BBerliner"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class PROFILE_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
