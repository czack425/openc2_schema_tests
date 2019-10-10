"""
OpenC2 General Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip


@unittest.skipIf(check_profiles_skip("general"), "General tests not specified")
class General_UseCases(SetupTests):
    def test_att_allow_domain_name(self):
        """
        Allow Domain Name
        src: ATT
        """
        cmd = {
            "action": "allow",
            "target": {
                "domain_name": "host1.company.com"
            },
            "args": {
                "response_requested": "complete"
            }
        }
        rsp = {
            "status": 200,
            "status_text": "host1.company.com uncontained"
        }

        self.validate(cmd, self.cmd_exp)
        self.validate(rsp, self.rsp_exp)

    def test_att_contain_domain_name(self):
        """
        Contain Domain Name
        src: ATT
        """
        cmd = {
            "action": "contain",
            "target": {
                "domain_name": "host1.company.com"
            },
            "args": {
                "response_requested": "complete"
            }
        }
        rsp = {
            "status": 200,
            "status_text": "host1.company.com contained"
        }

        self.validate(cmd, self.cmd_exp)
        self.validate(rsp, self.rsp_exp)

    def test_att_copy_domain_name(self):
        """
        Copy Domain Name
        src: ATT
        """
        cmd = {
            "action": "copy",
            "target": {
                "domain_name": "www.badguy.com"
            },
            "args": {
                "stop_time": 1528223143,  # 2018-06-05T18:25:43.511Z
                "signature_id": 277
            }
        }
        rsp = {
            "status": 200,
            "status_text": "host1.company.com contained"
        }

        with self.assertRaises(ValidationError):
            self.validate(cmd, self.cmd_exp)

        # TODO: get response
        # self.validate(rsp, self.rsp_exp)

    def test_att_locate_ip_addr(self):
        """
        Locate IPv4 Address
        src: ATT
        """
        cmd = {
            "action": "locate",
            "target": {
                "ipv4_addr": "198.51.100.0"
            }
        }
        rsp = {
            "status": 200,
            "extension": {
                "74": {
                    "iploc": {
                        "ip": {
                            "addr": "198.51.100.0",
                            "desc": "IANA"
                        },
                        "geo": {
                            "country": "Null Island",
                            "cc": "NI",
                            "lat": "0.00000",
                            "lon": "0.00000"
                        }
                    }
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate(cmd, self.cmd_exp)

        with self.assertRaises(ValidationError):
            self.validate(rsp, self.rsp_exp)

    def test_dod_scan_file(self):
        """
        Scan File
        src: DoD
        """
        cmd = {
            "action": "scan",
            "target": {
                "file": {
                    "hashes": {
                        "sha256": "04CDAFBCEE5F481ED8F6D585F5B7D14B54810D06FA44470A9726EA77DC25522E"
                    }
                }
            },
            "args": {
                "response_requested": "ack"
            },
            "command_id": "cmd5"
        }
        rsp = {
            "status": 102
        }

        self.validate(cmd, self.cmd_exp)
        self.validate(rsp, self.rsp_exp)

    def test_phantom_endpoint_list_processes(self):
        """
        Query Multiple Targets (Process, IPv4 Address)
        src: Phantom
        """
        cmd = {
            "action": "query",
            "target": {
                "process": {},
                "ipv4_addr": "198.51.100.7"
            }
        }
        rsp = {
            "status": 200,
            "status_text": "host1.company.com contained"
        }

        with self.assertRaises(ValidationError):
            self.validate(cmd, self.cmd_exp)

        # TODO: Get response
        # self.validate(rsp, self.rsp_exp)
