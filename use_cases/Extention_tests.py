"""
OpenC2 Extension Use Case Command/Response Pairs
"""
import unittest

from jsonschema.exceptions import ValidationError
from .test_setup import SetupTests
from .utils import check_profiles_skip


@unittest.skipIf(check_profiles_skip("extension"), "Custom Profile tests not specified")
class Extension_UseCases(SetupTests):
    def test_dod_status_requested(self):
        """
        Query Command
        src: DoD
        """
        cmd = {
            "action": "query",
            "target": {
                "command": "cmd5"
            },
            "args": {
                "response_requested": "status"
            }
        }
        rsp = {
            "status": 102,
            "results": {
                "x-acme": {
                    "status": "good"
                }
            }
        }

        self.validate(cmd, self.cmd_exp)
        self.validate(rsp, self.rsp_exp)

    def test_dod_cancel_command(self):
        """
        Cancel Command
        src: DoD
        """
        cmd = {
            "action": "cancel",
            "target": {
                 "command": "cmd5"
            }
        }
        rsp = {
            "status": 200,
            "results": {
                "x-acme": {
                    "status": "command canceled"
                }
            }
        }

        self.validate(cmd, self.cmd_exp)
        self.validate(rsp, self.rsp_exp)

    def test_dod_properties(self):
        """
        Query Properties
        src: DoD
        """
        cmd = {
            "action": "query",
            "target": {
                "properties": [
                    "battery_percentage"
                ]
            },
            "actuator": {
                "x-endpoint_smart_meter": {
                    "actuator_id": "TSLA-00101111",
                    "asset_id": "TGEadsasd"
                }
            },
            "command_id": "01076931758653239640628182951035"
        }
        rsp = {
            "status": 200,
            "results": {
                "x-acme": {
                    "battery_percentage": 0.577216
                }
            }
        }

        self.validate(cmd, self.cmd_exp)
        self.validate(rsp, self.rsp_exp)

    def test_phantom_endpoint_deny_process_with_hash(self):
        """
        Deny Process
        src: Phantom
        """
        cmd = {
            "action": "deny",
            "target": {
                "process": {
                    "executable": {
                        "hashes": {
                            "sha256": "19ce084ab0599c1659e4ce12ae822bd3"
                        }
                    }
                }
            },
            "actuator": {
                "x-endpoint": {
                    "key": "my_endpoint_actuator_name"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "host1.company.com contained"
        }

        self.validate_as(cmd, self.cmd_exp)

        # TODO: Get response
        # self.validate_as(rsp, self.rsp_exp)

    def test_phantom_endpoint_stop_process_by_pid(self):
        """
        Stop Multiple Targets (Process, Device)
        src: Phantom
        """
        cmd = {
            "action": "stop",
            "target": {
                "process": {
                    "pid": 1234
                },
                "device": {
                    "hostname": "198.51.100.131"
                }
            },
            "actuator": {
                "x-endpoint": "my_endpoint_actuator_name"
            }
        }
        rsp = {
            "status": 200,
            "status_text": "host1.company.com contained"
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        # TODO: Get response
        # self.validate_as(rsp, self.rsp_exp)

    def test_phantom_endpoint_delete_file(self):
        """
        Delete Multiple Targets (File, Device)
        src: Phantom
        """
        cmd = {
            "action": "delete",
            "target": {
                "file": {
                    "path": "C:\\Windows\\System32\\otaku.exe"
                },
                "device": {
                    "hostname": "198.51.100.131"
                }
            },
            "actuator": {
                "x-endpoint": "my_endpoint_actuator_name"
            }
        }
        rsp = {
            "status": 200,
            "status_text": "host1.company.com contained"
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        # TODO: Get response
        # self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_allow_device(self):
        """
        This action specifies that the endpoint actuator allow the device back online. e.g Remove from containment mode.
        src: Symantex
        """
        cmd = {
            "action": "allow",
            "target": {
                "device": {
                    "hostname": "endpoint6.example.com"
                }
            },
            "args": {
                "start_time": 1533144553,  # 2018-08-01T17:29:13.150Z
                "stop_time": 1533155353,  # 2018-08-01T20:29:13.150Z
                "duration": 0,
                "response_requested": "ack"
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_allow_file(self):
        """
        This action tells openC2 to allow the file on the computer. e.g In an endpoints case, whitelist.
        src: Symantex
        """
        cmd = {
            "action": "allow",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529935263,  # 2018-06-25T14:01:03.952Z
                "stop_time": 1529935270,  # 2018-06-25T14:01:10.952Z
                "duration": 0,
                "response_requested": "ack"
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_allow_url(self):
        """
        This action specifies that specified URL is allowed to be accessed.
        src: Symantex
        """
        cmd = {
            "action": "allow",
            "target": {
                "uri": "http://www.example.com"
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_contain_device(self):
        """
        This action specifies a device enter a quarantine state.
        src: Symantex
        """
        cmd = {
            "action": "contain",
            "target": {
                "device": {
                    "hostname": "endpoint6.example.com"
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_copy_file(self):
        """
        This action initiates the collection of a file of interest.
        src: Symantex
        """
        cmd = {
            "action": "copy",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529935158,  # 2018-06-25T13:59:18.332Z
                "stop_time": 1529935158,  # 2018-06-25T13:59:18.332Z
                "duration": 0,
                "response_requested": "ack",
                "search_location": "filesystem",
                "user_name": "string",
                "user_domain": "string",
                "password": "string"
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_delete_device(self):
        """
        This action specifies a device deletion from the managemed environment.
        src: Symantex
        """
        cmd = {
            "action": "delete",
            "target": {
                "device": {
                    "hostname": "endpoint6.example.com"
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_delete_file(self):
        """
        This action specifies a file to be deleted.
        src: Symantex
        """
        cmd = {
            "action": "delete",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529955077,  # 2018-06-25T19:31:17.916Z
                "stop_time": 1529955077,  # 2018-06-25T19:31:17.916Z
                "duration": 0,
                "response_requested": "ack",
                "remediation": {
                    "override_process_termination": True
                },
                "allow_quick_search": True,
                "scan_network_paths": True,
                "limit_result_count": 0
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_deny_file(self):
        """
        This action specifies a file be denied on an endpoint. e.g Deny file from being written to disk.
        src: Symantex
        """
        cmd = {
            "action": "deny",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529955583,  # 2018-06-25T19:39:43.246Z
                "stop_time": 1529955583,  # 2018-06-25T19:39:43.246Z
                "duration": 0,
                "response_requested": "ack"
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_deny_process(self):
        """
        This action specifies a process be denied execution on an endpoint.
        src: Symantex
        """
        cmd = {
            "action": "deny",
            "target": {
                "process": {
                    "name": "otaku.exe",
                    "pid": 0
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_investigate_device(self):
        """
        This action gets descriptive data about processes or load point information that have run or have been accessed recently.
        src: Symantex
        """
        cmd = {
            "action": "investigate",
            "target": {
                "device": {
                    "hostname": "endpoint6.example.com"
                }
            },
            "args": {
                "start_time": 1529934935,  # 2018-06-25T13:55:35.341Z
                "stop_time": 1529934935,  # 2018-06-25T13:55:35.341Z
                "duration": 0,
                "response_requested": "ack",
                "include_running": True,
                "include_historical": True,
                "include_prefetch": True,
                "include_loadpoints": True
            },
            "actuator": {
                "x-process_anti_virus_scanner": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_locate_process(self):
        """
        This action triggers a scan to locate the process.
        src: Symantex
        """
        cmd = {
            "action": "locate",
            "target": {
                "process": {
                    "name": "otaku.exe",
                    "pid": 0
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_query_device(self):
        """
        This action retrieves all available information on the specified device collected by the actuator.
        src: Symantex
        """
        cmd = {
            "action": "query",
            "target": {
                "device": {
                    "hostname": "endpoint6.example.com"
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_query_file(self):
        """
        This action queries for the existance of a particular file.
        src: Symantex
        """
        cmd = {
            "action": "query",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529935263,  # 2018-06-25T14:01:03.952Z
                "stop_time": 1529935263,  # 2018-06-25T14:01:03.952Z
                "duration": 0,
                "response_requested": "ack",
                "remediation": {
                    "override_process_termination": True,
                    "scan_guid": "string"
                },
                "allow_quick_search": True,
                "scan_network_paths": True,
                "limit_result_count": 0
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_query_software(self):
        """
        This action retrieves all available information on the specified software on the actuator.
        src: Symantex
        """
        cmd = {
            "action": "query",
            "target": {
                "software": {
                    "vendor": "vendor_string",
                    "name": "otaku.exe",
                    "language": "en-us",
                    "version": "1.0"
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_remediate_file(self):
        """
        This action remediates the threat.
        src: Symantex
        """
        cmd = {
            "action": "remediate",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529935263,  # 2018-06-25T14:01:03.952Z
                "stop_time": 1529935263,  # 2018-06-25T14:01:03.952Z
                "duration": 0,
                "response_requested": "ack",
                "remediation": {
                    "override_process_termination": True,
                    "scan_guid": "string"
                },
                "allow_quick_search": True,
                "scan_network_paths": True,
                "limit_result_count": 0
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_restart_device(self):
        """
        This action restarts a device based on its asset_id.
        src: Symantex
        """
        cmd = {
            "action": "restart",
            "target": {
                "device": {
                    "hostname": "endpoint6.example.com"
                }
            },
            "args": {
                "start_time": 1529934732,  # 2018-06-25T13:52:12.691Z
                "stop_time": 1529934732,  # 2018-06-25T13:52:12.691Z
                "duration": 0,
                "response_requested": "ack",
                "allow_delay": True,
                "occurance": "now",
                "restart_time": "string",
                "randomize": True,
                "prompt": True,
                "prompt_message": "string"
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_restart_process(self):
        """
        This action specifies a process to restart.
        src: Symantex
        """
        cmd = {
            "action": "restart",
            "target": {
                "process": {
                    "name": "otaku.exe"
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_start_process(self):
        """
        This action specifies a process to start.
        src: Symantex
        """
        cmd = {
            "action": "start",
            "target": {
                "process": {
                    "name": "otaku.exe"
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_stop_process(self):
        """
        This action stops a specific process.
        src: Symantex
        """
        cmd = {
            "action": "stop",
            "target": {
                "process": {
                    "pid": 0,
                    "name": "netgato.exe",
                    "cwd": "string"
                }
            },
            "args": {
                "start_time": 1529934593,  # 2018-06-25T13:49:53.030Z
                "stop_time": 1529934593,  # 2018-06-25T13:49:53.030Z
                "duration": 0,
                "response_requested": "ack",
                "remediation": {
                    "override_process_termination": True
                },
                "allow_quick_search": True,
                "scan_network_paths": True,
                "limit_result_count": 0
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_update_device(self):
        """
        This action triggers a content update session from the update server.
        src: Symantex
        """
        cmd = {
            "action": "update",
            "target": {
                "device": {
                    "hostname": "endpoint6.example.com"
                }
            },
            "args": {
                "start_time": 1529937575,  # 2018-06-25T14:39:35.166Z
                "stop_time": 1529937575,  # 2018-06-25T14:39:35.166Z
                "duration": 0,
                "response_requested": "ack"
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_endpoint_update_software(self):
        """
        This action updates the specified software.
        src: Symantex
        """
        cmd = {
            "action": "update",
            "target": {
                "software": {
                    "name": "otaku.exe",
                    "language": "en-us",
                    "vendor": "vendorString",
                    "version": "14"
                }
            },
            "actuator": {
                "x-endpoint": {
                    "asset_id": "endpoint6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_network_proxy_deny_url(self):
        """
        This action specifies a url be blocked from access.
        src: Symantex
        """
        cmd = {
            "action": "deny",
            "target": {
                "uri": "http://village.example.com"
            },
            "actuator": {
                "x-network_proxy": {
                    "asset_id": "gateway2.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_network_proxy_query_url(self):
        """
        This action retrieves all available information on the specified URL on the actuator.
        src: Symantex
        """
        cmd = {
            "action": "query",
            "target": {
                "uri": "http://village.example.com"
            },
            "actuator": {
                "x-network_proxy": {
                    "asset_id": "gateway2.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_openc2_cancel_command(self):
        """
        This action cancels a previously sent openc2 command.
        src: Symantex
        """
        cmd = {
            "action": "cancel",
            "target": {
                "command": "07488298-0ce1-408f-80ab-0013e8973266"
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_anti_virus_scanner_locate_directory(self):
        """
        This action triggers a scan to locate the directory path location.
        src: Symantex
        """
        cmd = {
            "action": "locate",
            "target": {
                "directory": {
                    "path": "string"
                }
            },
            "args": {
                "start_time": 1529937996,  # 2018-06-25T14:46:36.786Z
                "stop_time": 1529937996,  # 2018-06-25T14:46:36.786Z
                "duration": 0,
                "response_requested": "ack",
                "allow_quick_search": True,
                "scan_network_paths": True,
                "limit_result_count": 0
            },
            "actuator": {
                "x-process_anti_virus_scanner": {
                    "asset_id": "device6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_anti_virus_scanner_locate_file(self):
        """
        This action triggers a scan to locate the file.
        src: Symantex
        """
        cmd = {
            "action": "locate",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529934321,  # 2018-06-25T13:45:21.908Z
                "stop_time": 1529934321,  # 2018-06-25T13:45:21.908Z
                "duration": 0,
                "response_requested": "ack",
                "allow_quick_search": True,
                "scan_network_paths": True,
                "limit_result_count": 0
            },
            "actuator": {
                "x-process_anti_virus_scanner": {
                    "asset_id": "device6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_anti_virus_scanner_locate_windows_registry_key(self):
        """
        This action triggers a scan to locate the windows registry key.
        src: Symantex
        """
        cmd = {
            "action": "locate",
            "target": {
                "windows_registry_key": {
                    "key": "string"
                }
            },
            "args": {
                "start_time": 1529938054,  # 2018-06-25T14:47:34.109Z
                "stop_time": 1529938054,  # 2018-06-25T14:47:34.109Z
                "duration": 0,
                "response_requested": "ack",
                "allow_quick_search": True,
                "scan_network_paths": True,
                "limit_result_count": 0
            },
            "actuator": {
                "x-process_anti_virus_scanner": {
                    "asset_id": "device6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_anti_virus_scanner_restore_file(self):
        """
        This action restores a file that was previously quarantined or isolated in some manner.
        src: Symantex
        """
        cmd = {
            "action": "restore",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529934817,  # 2018-06-25T13:53:37.231Z
                "stop_time": 1529934817,  # 2018-06-25T13:53:37.231Z
                "duration": 0,
                "response_requested": "ack"
            },
            "actuator": {
                "x-process_anti_virus_scanner": {
                    "asset_id": "device6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_anti_virus_scanner_scan_file(self):
        """
        This action scans for a particular file using the anti-virus scanner component.
        src: Symantex
        """
        cmd = {
            "action": "scan",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529934374,  # 2018-06-25T13:46:14.013Z
                "stop_time": 1529934374,  # 2018-06-25T13:46:14.013Z
                "duration": 0,
                "response_requested": "ack",
                "type": "QUICK"
            },
            "actuator": {
                "x-process_anti_virus_scanner": {
                    "asset_id": "device6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_email_service_deny_email_addr(self):
        """
        This action specifies an email address be denied.
        src: Symantex
        """
        cmd = {
            "action": "deny",
            "target": {
                "email_addr": "number6@village.example.com"
            },
            "actuator": {
                "x-process_email_service": {
                    "asset_id": "mailserver6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_email_service_deny_email_message(self):
        """
        This action specifies that an email matching email-message target values be denied.
        src: Symantex
        """
        cmd = {
            "action": "deny",
            "target": {
                "email_message": {
                    "to": "string@string",
                    "from": "string@string",
                    "subject": "string",
                    "cc": "string@string",
                    "bcc": "string@string"
                }
            },
            "actuator": {
                "x-process_email_service": {
                    "asset_id": "mailserver6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)

        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_sandbox_detonate_file(self):
        """
        This action submits a suspicious file for analysis.
        src: Symantex
        """
        cmd = {
            "action": "detonate",
            "target": {
                "file": {
                    "name": "netgato.exe",
                    "hashes": {
                        "sha256": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
                    }
                }
            },
            "args": {
                "start_time": 1529935039,  # 2018-06-25T13:57:19.030Z
                "stop_time": 1529935039,  # 2018-06-25T13:57:19.030Z
                "duration": 0,
                "response_requested": "ack"
            },
            "actuator": {
                "x-process_sandbox": {
                    "asset_id": "sandbox6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)

    def test_symantex_process_sandbox_detonate_url(self):
        """
        This action submits a url for sandbox detonation.
        src: Symantex
        """
        cmd = {
            "action": "detonate",
            "target": {
                "uri": "http://two.village.example.com"
            },
            "actuator": {
                "x-process_sandbox": {
                    "asset_id": "sandbox6.example.com"
                }
            }
        }
        rsp = {
            "status": 200,
            "status_text": "string",
            "results": {
                "x-command": {
                    "ref": "INTERNALREFERENCEVALUEABC123"
                }
            }
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)
