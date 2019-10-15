"""
OpenC2 Stateful Packet Filtering Profile (SFPF) Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "SFPF"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class SFPF_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
