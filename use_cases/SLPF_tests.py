"""
OpenC2 Stateless Packet Filtering Profile (SLPF) Use Case Command/Response Pairs
"""
import unittest

from .test_setup import SetupTests, ValidationError
from .utils import check_profiles_skip

profile = "SLPF"


@unittest.skipIf(check_profiles_skip(profile), f"{profile} Profile tests not specified")
class SLPF_UseCases(SetupTests):
    # Dynamic Validation Variables
    profile = profile

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

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

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

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)
