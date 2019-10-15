"""
OpenC2 Test case Setup
"""
import copy
import json
import os
import re
import unittest

from abc import ABCMeta
from functools import partialmethod
from jsonschema import Draft7Validator, ValidationError
from typing import (
    Any,
    Tuple
)

from .utils import clean_var_name, load_cases, short_exception, ExtendedResolver


class TestMeta(ABCMeta):
    def __new__(mcs, name, bases, namespace):
        new_namespace = dict(namespace)
        profile = new_namespace.pop("profile", None)
        if profile:
            base_cls = bases[0]

            for case, tests in load_cases(profile).items():
                case = re.sub(r"s$", "", case)
                test_fun = getattr(base_cls, f"{case}_test", None)
                if test_fun is None:
                    raise AttributeError(f"{name}: Missing base test function for {case}")

                for msg_name, msg in tests.items():
                    fun_name = f"test_{case}_{clean_var_name(msg_name)}"
                    if fun_name in new_namespace:
                        raise AttributeError(f"{name}: Test function already exists for {fun_name}")

                    new_namespace[fun_name] = partialmethod(test_fun, msg=msg)

        return super().__new__(mcs, name, bases, new_namespace)


class SetupTests(unittest.TestCase, metaclass=TestMeta):
    schema_file: str = None
    root_dir: str = None
    cmd_exp: str = "OpenC2-Command"
    rsp_exp: str = "OpenC2-Response"
    # Override in subclass
    profile: str

    def loadSchema(self, schema: dict = None) -> Tuple[dict, ExtendedResolver]:
        """
        Perform Test SetUp
        Load schema from file
        """
        if schema is None:
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

    @short_exception
    def validate(self, msg: Any):
        """
        Validate as generic instance against the schema
        :param msg: instance to validate
        :return:
        """
        schema, resolver = self.loadSchema()
        validator = Draft7Validator(
            schema=schema,
            resolver=resolver
        )
        return validator.validate(msg)

    @short_exception
    def validate_as(self, msg: Any, _type: str):
        """
        Validate as specified instance against the schema
        Schema altered for better error messages
        :param msg: instance to validate
        :param _type: specific oneOf type to validate as
        :return:
        """
        schema, resolver = self.loadSchema()
        export = [e for e in schema["oneOf"] if _type == re.sub(r"#/definitions/", "", e.get("$ref", ""))]
        if export and "oneOf" in schema:
            tmp_schema = copy.deepcopy(schema)
            del tmp_schema["oneOf"]
            tmp_schema.update(export[0])

            schema, resolver = self.loadSchema(tmp_schema)
            validator = Draft7Validator(
                schema=tmp_schema,
                resolver=resolver
            )
            return validator.validate(msg)
        raise TypeError(f"{_type} is not a valid oneOf as defined in the schema")

    # Dynamic Validation Functions
    def good_command_test(self, msg):
        """
        Test a good command, should not result in an exception
        """
        self.validate_as(msg, self.cmd_exp)

    def bad_command_test(self, msg):
        """
        Test a bad command, should result in an exception
        """
        with self.assertRaises(ValidationError):
            self.validate_as(msg, self.cmd_exp)

    def good_response_test(self, msg):
        """
        Test a good response, should not result in an exception
        """
        self.validate_as(msg, self.rsp_exp)

    def bad_response_test(self, msg):
        """
        Test a bad response, should result in an exception
        """
        with self.assertRaises(ValidationError):
            self.validate_as(msg, self.rsp_exp)
