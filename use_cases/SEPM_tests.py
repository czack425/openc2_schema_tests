"""
OpenC2 Symantec: Endpoint Protection Manager Custom Profile (SEPM) Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "X_SEPM"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class SEPM_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

    # Static Validation Functions
