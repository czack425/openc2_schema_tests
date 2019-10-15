"""
OpenC2 Symantec: Integrated Cyber Defense Exchange Custom Profile (ICDX) Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "X_ICDX"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class ICDX_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
