"""
OpenC2 Test case Setup
"""
import json
import os
import unittest

from jsonschema import Draft7Validator
from typing import (
    Any,
    Tuple
)

from . import file_dir
from .utils import ExtendedResolver

schema_dir = os.path.join(file_dir, "..", "schemas")


class SetupTests(unittest.TestCase):
    schema_file: str = None
    root_dir: str = None
    cmd_exp: str = "OpenC2-Command"
    rsp_exp: str = "OpenC2-Response"

    def loadSchema(self) -> Tuple[dict, ExtendedResolver]:
        """
        Perform Test SetUp
        Load schema from file
        """
        if self.schema_file:
            self.schema_file = os.path.abspath(self.schema_file)
            if os.path.isfile(self.schema_file):
                with open(self.schema_file, "r") as schema_file:
                    schema = json.load(schema_file)
            else:
                schema = json.loads(self.schema_file)
        else:
            raise AttributeError("Attribute `schema_file` is not valid")

        resolver = None
        if self.root_dir:
            resolver = ExtendedResolver.from_schema(
                schema=schema,
                **{"root_dir": os.path.abspath(self.root_dir)} if self.root_dir else {}
            )

        return schema, resolver

    def validate(self, msg: Any, _type: str = None):
        schema, resolver = self.loadSchema()
        validator = Draft7Validator(
            schema=schema,
            resolver=resolver
        )
        if _type:
            # Validate as specific type
            return validator.validate(msg)

        # Validate as generic
        return validator.validate(msg)


def check_profile_skip(*profiles: str) -> bool:
    profiles_orig = os.getenv("testProfiles", "").split(",")
    profiles_lower = list(map(str.lower, profiles_orig))

    if len({*profiles} - {*profiles_lower}) == 0:
        matches = list(map(profiles_orig.pop, list(map(profiles_lower.index, profiles))))
        os.environ["testProfiles"] = ",".join(profiles_orig)
        return False
    return True
