"""
OpenC2 Stateless Packet Filtering Profile (SLPF) Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from parameterized import parameterized
from .test_setup import SetupTests
from .utils import check_profiles_skip, load_cases

profile = "SLPF"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class SLPF_UseCases(SetupTests):
    good_commands = load_cases(profile, "commands-good")
    bad_commands = load_cases(profile, "commands-bad")
    good_responses = load_cases(profile, "response-good")
    bad_responses = load_cases(profile, "response-bad")

    # Dynamic Validation Functions
    @unittest.skipIf(good_commands == [], f"{profile}: no good command test cases")
    @parameterized.expand(load_cases(profile, "commands-good"), skip_on_empty=True)
    def test_good_commands(self, name, msg):
        self.validate(msg, self.cmd_exp)

    @unittest.skipIf(bad_commands == [], f"{profile}: no bad command test cases")
    @parameterized.expand(load_cases(profile, "commands-bad"), skip_on_empty=True)
    def test_bad_commands(self, name, msg):
        with self.assertRaises(ValidationError):
            self.validate(msg, self.cmd_exp)

    @unittest.skipIf(good_responses == [], f"{profile}: no good response test cases")
    @parameterized.expand(load_cases(profile, "response-good"), skip_on_empty=True)
    def test_good_response(self, name, msg):
        self.validate(msg, self.cmd_exp)

    @unittest.skipIf(bad_responses == [], f"{profile}: no bad response test cases")
    @parameterized.expand(load_cases(profile, "response-bad"), skip_on_empty=True)
    def test_bad_response(self, name, msg):
        with self.assertRaises(ValidationError):
            self.validate(msg, self.cmd_exp)

    # Static Validation Functions
    def test_att_allow_slpf(self):
        """
        Allow SLPF
        src: ATT
        """
        cmd = {
            "action": "allow",
            "target": {
                "ipv4_connection": {
                    "src_addr": "1.2.3.4",
                    "dst_port": 443,
                    "protocol": "tcp"
                }
            },
            "args": {
                "response_requested": "complete",
                "slpf": {
                    "insert_rule": 101,
                    "direction": "ingress",
                }
            },
            "actuator": {
                "slpf": {
                    "asset_id": "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-01234567"
                }
            }
        }
        rsp = {
            "status": 200,
            "results": {
                "slpf": {
                    "rule_number": 101
                }
            }
        }

        self.validate(cmd, self.cmd_exp)
        self.validate(rsp, self.rsp_exp)

    def test_att_deny_slpf(self):
        """
        Deny SLPF
        src: ATT
        """
        cmd = {
            "action": "deny",
            "target": {
                "ipv4_connection": {
                    "src_addr": "1.2.3.4",
                    "dst_port": 80,
                    "protocol": "tcp"
                }
            },
            "args": {
                "response_requested": "complete",
                "slpf": {
                    "insert_rule": 100,
                    "direction": "ingress",
                }
            },
            "actuator": {
                "slpf": {
                    "asset_id": "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-01234567"
                }
            }

        }
        rsp = {
            "status": 200,
            "results": {
                "slpf": {
                    "rule_number": 100
                }
            }
        }

        self.validate(cmd, self.cmd_exp)
        self.validate(rsp, self.rsp_exp)
