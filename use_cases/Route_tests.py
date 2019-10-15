"""
OpenC2 Packet Routing Profile Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "Route"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class Route_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
