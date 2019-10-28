"""
OpenC2 DoD: Packet Routing Custom Profile Custom Profile Use Case Command/Response Pairs Template
"""
import unittest

from .test_setup import SetupTests, ValidationError
from .utils import check_profiles_skip

profile = "X_Route"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class X_Route_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
