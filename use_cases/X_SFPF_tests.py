"""
OpenC2 U. of Oslo: Stateful Packet Filtering Custom Profile Use Case Command/Response Pairs Template
"""
import unittest

from .test_setup import SetupTests, ValidationError
from .utils import check_profiles_skip

profile = "X_SFPF"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class X_SFPF_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
