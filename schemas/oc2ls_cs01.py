"""
OpenC2 Language Specification version 1.0 csprd01
"""
from jadnschema_code import SchemaModel
from jadnschema_code.structures import *
from jadnschema_code.utils import definition, export

Valid_Extensions = ("slpf", )

# Primitive Types
# Binary
@definition
class IPv4_Addr(Binary):
    """
    32 bit IPv4 address as defined in [RFC0791]
    """
    alias = "IPv4-Addr"
    format = "ipv4-addr"


@definition
class IPv6_Addr(Binary):
    """
    128 bit IPv6 address as defined in [RFC8200]
    """
    alias = "IPv6-Addr"
    format = "ipv6-addr"


@definition
class MAC_Addr(Binary):
    """
    Media Access Control / Extended Unique Identifier address - EUI-48 or EUI-64 as defined in [EUI]
    """
    alias = "MAC-Addr"
    format = "eui"


# Integer
@definition
class Date_Time(Integer):
    """
    Date and Time
    """
    alias = "Date-Time"
    minimum = 0


@definition
class Duration(Integer):
    """
    A length of time
    """
    minimum = 0


@definition
class Port(Integer):
    """
    Transport Protocol Port Number, [RFC6335]
    """
    minimum = 0
    maximum = 65535


# String
@definition
class Command_ID(String):
    """
    Command Identifier
    """
    alias = "Command-ID"


@definition
class Domain_Name(String):
    """
    [RFC1034], Section 3.5
    """
    alias = "Domain-Name"
    format = "hostname"


@definition
class Email_Addr(String):
    """
    Email address - [RFC5322], Section 3.4.1
    """
    alias = "Email-Addr"
    format = "email"


@definition
class Hostname(String):
    """
    Internet host name as specified in [RFC1123]
    """
    format = "hostname"


@definition
class IDN_Domain_Name(String):
    """
    Internationalized Domain Name - [RFC5890], Section 2.3.2.3
    """
    alias = "IDN-Domain-Name"
    format = "idn-hostname"


@definition
class IDN_Email_Addr(String):
    """
    Internationalized email address - [RFC6531]
    """
    alias = "IDN-Email-Addr"
    format = "idn-email"


@definition
class IDN_Hostname(String):
    """
    Internationalized Internet host name as specified in [RFC5890], Section 2.3.2.3
    """
    alias = "IDN-Hostname"
    format = "idn-hostname"


@definition
class IRI(String):
    """
    Internationalized Resource Identifier, [RFC3987]
    """
    format = "iri"


@definition
class Nsid(String):
    """
    A short identifier that refers to a namespace
    """
    minimum = 1
    maximum = 16
    pattern = rf"^({'|'.join(Valid_Extensions)}|x-.*)$"


@definition
class URI(String):
    """
    Uniform Resource Identifier, [RFC3986]
    """
    format = "uri"


@definition
class Version(String):
    """
    Major.Minor version number
    """
    pattern = r"^\d+\.\d+(\.\d+)?$"


# Structure Types
# Enumerated Structures
@definition
class Action(EnumeratedModel):
    scan = Enum(id=1, desc="Systematic examination of some aspect of the entity or its environment")
    locate = Enum(id=2, desc="Find an object physically, logically, functionally, or by organization")
    query = Enum(id=3, desc="Initiate a request for information")
    deny = Enum(id=6, desc="Prevent a certain event or action from completion, such as preventing a flow from reaching a destination or preventing access")
    contain = Enum(id=7, desc="Isolate a file, process, or entity so that it cannot modify or access assets or processes")
    allow = Enum(id=8, desc="Permit access to or execution of a Target")
    start = Enum(id=9, desc="Initiate a process, application, system, or activity")
    stop = Enum(id=10, desc="Halt a system or end an activity")
    restart = Enum(id=11, desc="Stop then start a system or an activity")
    cancel = Enum(id=14, desc="Invalidate a previously issued Action")
    set_ = Enum(id=15, value="set", desc="Change a value, configuration, or state of a managed entity")
    update = Enum(id=16, desc="Instruct a component to retrieve, install, process, and operate in accordance with a software update, reconfiguration, or other update")
    redirect = Enum(id=18, desc="Change the flow of traffic to a destination other than its original destination")
    create = Enum(id=19, desc="Add a new entity of a known type (e.g., data, files, directories)")
    delete = Enum(id=20, desc="Remove an entity (e.g., data, files, flows)")
    detonate = Enum(id=22, desc="Execute and observe the behavior of a Target (e.g., file, hyperlink) in an isolated environment")
    restore = Enum(id=23, desc="Return a system to a previously known state")
    copy = Enum(id=28, desc="Duplicate an object, file, data flow, or artifact")
    investigate = Enum(id=30, desc="Task the recipient to aggregate and report information as it pertains to a security event or incident")
    remediate = Enum(id=32, desc="Task the recipient to eliminate a vulnerability or attack point")


@definition
class Feature(EnumeratedModel):
    """
    Specifies the results to be returned from a query features Command
    """
    versions = Enum(id=1, desc="List of OpenC2 Language versions supported by this Actuator")
    profiles = Enum(id=2, desc="List of profiles supported by this Actuator")
    pairs = Enum(id=3, desc="List of supported Actions and applicable Targets")
    rate_limit = Enum(id=4, desc="Maximum number of Commands per minute supported by design or policy")


@definition
class L4_Protocol(EnumeratedModel):
    """
    Value of the protocol (IPv4) or next header (IPv6) field in an IP packet. Any IANA value, [RFC5237]
    """
    icmp = Enum(id=1, desc="Internet Control Message Protocol - [RFC0792]")
    tcp = Enum(id=6, desc="Transmission Control Protocol - [RFC0793]")
    udp = Enum(id=17, desc="User Datagram Protocol - [RFC0768]")
    sctp = Enum(id=132, desc="Stream Control Transmission Protocol - [RFC4960]")

    class Options:
        alias = "L4-Protocol"


@definition
class Response_Type(EnumeratedModel):
    none = Enum(id=0, desc="No response")
    ack = Enum(id=1, desc="Respond when Command received")
    status = Enum(id=2, desc="Respond with progress toward Command completion")
    complete = Enum(id=3, desc="Respond when all aspects of Command completed")

    class Options:
        alias = "Response-Type"


@definition
class Status_Code(EnumeratedModel):
    processing = Enum(id=102, value="Processing", desc="an interim Response used to inform the Producer that the Consumer has accepted the Command but has not yet completed it")
    ok = Enum(id=200, value="OK", desc="the Command has succeeded")
    bad_request = Enum(id=400, value="Bad Request", desc="the Consumer cannot process the Command due to something that is perceived to be a Producer error (e.g., malformed Command syntax)")
    unauthorized = Enum(id=401, value="Unauthorized", desc="the Command Message lacks valid authentication credentials for the target resource or authorization has been refused for the submitted credentials")
    forbidden = Enum(id=403, value="Forbidden", desc="the Consumer understood the Command but refuses to authorize it")
    not_found = Enum(id=404, value="Not Found", desc="the Consumer has not found anything matching the Command")
    internal_error = Enum(id=500, value="Internal Error", desc="the Consumer encountered an unexpected condition that prevented it from performing the Command")
    not_implemented = Enum(id=501, value="Not Implemented", desc="the Consumer does not support the functionality required to perform the Command")
    service_unavailable = Enum(id=503, value="Service Unavailable", desc="the Consumer is currently unable to perform the Command due to a temporary overloading or maintenance of the Consumer")

    class Options:
        alias = "Status-Code"
        compact = True


# Following Structures not grouped due to dependencies
@definition
class Actuator(MapModel):
    class Options:
        maximum = 1
        patternProperties = [
            {
                "pattern": rf"^({'|'.join(Valid_Extensions)})$",
                "type": SchemaTypes.Object,
                "description": "Language specification validator for committee approved actuators. In practice actuators should be a static property and this catch all should be removed",
                "minimum": 1
            },
            {
                "pattern": r"^x-[A-Za-z0-9]\w+$",
                "type": SchemaTypes.Object,
                "description": "Language specification validator for custom actuators. In practice actuators should be a static property and this catch all should be removed",
                "minimum": 1
            }
        ]


@definition
class Properties(ArrayOfModel):
    """
    A list of names that uniquely identify properties of an Actuator
    """
    valueType = String
    minimum = 1
    unique = True


@definition
class Hashes(MapModel):
    """
    Cryptographic Hash values
    """
    md5 = Field(id=1, type=Binary(format="x"), desc="MD5 hash as defined in [RFC1321]")
    sha1 = Field(id=2, type=Binary(format="x"), desc="SHA1 hash as defined in [RFC6234]")
    sha256 = Field(id=3, type=Binary(format="x"), desc="SHA256 hash as defined in [RFC6234]")


@definition
class Args(MapModel):
    start_time = Field(id=1, type=Date_Time, desc="The specific date/time to initiate the Command")
    stop_time = Field(id=2, type=Date_Time, desc="The specific date/time to terminate the Command")
    duration = Field(id=3, type=Duration, desc="The length of time for a Command to be in effect")
    response_requested = Field(id=4, type=Response_Type, desc="The type of Response required for the Command: none, ack, status, complete")

    class Options:
        patternProperties = [
            {
                "pattern": rf"^({'|'.join(Valid_Extensions)})$",
                "type": SchemaTypes.Object,
                "description": "Language specification validator for committee approved args extensions. In practice args extension should be a static property and this catch all should be removed",
                "minimum": 1
            },
            {
                "pattern": r"^x-[A-Za-z0-9]\w+$",
                "type": SchemaTypes.Object,
                "description": "Language specification validator for custom args extensions. In practice args extension should be a static property and this catch all should be removed",
                "minimum": 1
            }
        ]


@definition
class Versions(ArrayOfModel):
    """
    List of OpenC2 language versions supported by this Actuator
    """
    valueType = Version
    minimum = 1
    unique = True


@definition
class Profiles(ArrayOfModel):
    """
    List of profiles supported by this Actuator
    """
    valueType = Nsid
    minimum = 1
    unique = True


@definition
class Device(MapModel):
    hostname = Field(id=1, type=Hostname, desc="A hostname that can be used to connect to this device over a network")
    idn_hostname = Field(id=2, type=IDN_Hostname, desc="An internationalized hostname that can be used to connect to this device over a network")
    device_id = Field(id=3, type=String, desc="An identifier that refers to this device within an inventory or management system")


@definition
class Features(ArrayOfModel):
    """
    An array of zero to ten names used to query an Actuator for its supported capabilities
    """
    valueType = Feature
    minimum = 0
    maximum = 10
    unique = True


@definition
class File(MapModel):
    name = Field(id=1, type=String, desc="The name of the file as defined in the file system")
    path = Field(id=2, type=String, desc="The absolute path to the location of the file in the file system")
    hashes = Field(id=3, type=Hashes, desc="One or more cryptographic hash codes of the file contents")


@definition
class IPv4_Net(ArrayModel):
    """
    IPv4 address and prefix length
    """
    ipv4_addr = Field(id=1, type=IPv4_Addr, options=dict(required=True), desc="IPv4 address as defined in [RFC0791]")
    prefix_length = Field(id=2, type=Integer, desc="CIDR prefix-length. If omitted, refers to a single host address")

    class Options:
        alias = "IPv4-Net"
        format = "ipv4-net"


@definition
class IPv4_Connection(RecordModel):
    """
    5-tuple that specifies a tcp/ip connection
    """
    src_addr = Field(id=1, type=IPv4_Net, desc="IPv4 source address range")
    src_port = Field(id=2, type=Port, desc="Source service per [RFC6335]")
    dst_addr = Field(id=3, type=IPv4_Net, desc="IPv4 destination address range")
    dst_port = Field(id=4, type=Port, desc="Destination service per [RFC6335]")
    protocol = Field(id=5, type=L4_Protocol, desc="Layer 4 protocol (e.g., TCP) - see L4-Protocol section")

    class Options:
        alias = "IPv4-Connection"
        minimum = 1


@definition
class IPv6_Net(ArrayModel):
    """
    IPv6 address and prefix length
    """
    ipv6_addr = Field(id=1, type=IPv6_Addr, options=dict(required=True), desc="IPv6 address as defined in [RFC8200]")
    prefix_length = Field(id=2, type=Integer, desc="CIDR prefix-length. If omitted, refers to a single host address")

    class Options:
        alias = "IPv6-Net"
        format = "ipv6-net"


@definition
class IPv6_Connection(RecordModel):
    """
    5-tuple that specifies a tcp/ip connection
    """
    src_addr = Field(id=1, type=IPv6_Net, desc="IPv6 source address range")
    src_port = Field(id=2, type=Port, desc="Source service per [RFC6335]")
    dst_addr = Field(id=3, type=IPv6_Net, desc="IPv6 destination address range")
    dst_port = Field(id=4, type=Port, desc="Destination service per [RFC6335]")
    protocol = Field(id=5, type=L4_Protocol, desc="Layer 4 protocol (e.g., TCP) - see L4-Protocol section")

    class Options:
        alias = "IPv6-Connection"
        minimum = 1


@definition
class Process(MapModel):
    pid = Field(id=1, type=Integer(minimum=0), desc="Process ID of the process")
    name = Field(id=2, type=String, desc="Name of the process")
    cwd = Field(id=3, type=String, desc="Current working directory of the process")
    executable = Field(id=4, type=File, desc="Executable that was executed to start the process")
    parent = Field(id=5, type=Integer(minimum=0), desc="Process that spawned this one")
    command_line = Field(id=6, type=String, desc="The full command line invocation used to start this process, including all arguments")


@definition
class Payload(ChoiceModel):
    bin_ = Field(id=1, alias="bin", type=Binary, desc="Specifies the data contained in the artifact")
    url = Field(id=2, type=URI, desc="MUST be a valid URL that resolves to the un-encoded content")


@definition
class Artifact(RecordModel):
    mime_type = Field(id=1, type=String(pattern=r"^\w+\/[-+.\w]+$"), desc="Permitted values specified in the IANA Media Types registry, [RFC6838]")
    payload = Field(id=2, type=Payload, desc="Choice of literal content or URL")
    hashes = Field(id=3, type=Hashes, desc="Hashes of the payload content")

    class Options:
        minimum = 1


@definition
class Target(ChoiceModel):
    artifact = Field(id=1, type=Artifact, desc="An array of bytes representing a file-like object or a link to that object")
    command = Field(id=2, type=Command_ID, desc="A reference to a previously issued Command")
    device = Field(id=3, type=Device, desc="The properties of a hardware device")
    domain_name = Field(id=7, type=Domain_Name, desc="A network domain name")
    email_addr = Field(id=8, type=Email_Addr, desc="A single email address")
    features = Field(id=9, type=Features, desc="A set of items used with the query Action to determine an Actuator's capabilities")
    file = Field(id=10, type=File, desc="Properties of a file")
    idn_domain_name = Field(id=11, type=IDN_Domain_Name, desc="An internationalized domain name")
    idn_email_addr = Field(id=12, type=IDN_Email_Addr, desc="A single internationalized email address")
    ipv4_net = Field(id=13, type=IPv4_Net, desc="An IPv4 address range including CIDR prefix length")
    ipv6_net = Field(id=14, type=IPv6_Net, desc="An IPv6 address range including prefix length")
    ipv4_connection = Field(id=15, type=IPv4_Connection, desc="A 5-tuple of source and destination IPv4 address ranges, source and destination ports, and protocol")
    ipv6_connection = Field(id=16, type=IPv6_Connection, desc="A 5-tuple of source and destination IPv6 address ranges, source and destination ports, and protocol")
    iri = Field(id=20, type=IRI, desc="An internationalized resource identifier (IRI)")
    mac_addr = Field(id=17, type=MAC_Addr, desc="A Media Access Control (MAC) address - EUI-48 or EUI-64 as defined in [EUI]")
    process = Field(id=18, type=Process, desc="Common properties of an instance of a computer program as executed on an operating system")
    properties = Field(id=25, type=Properties, desc="Data attribute associated with an Actuator")
    uri = Field(id=19, type=URI, desc="A uniform resource identifier (URI)")

    class Options:
        patternProperties = [
            {
                "pattern": rf"^({'|'.join(Valid_Extensions)}):[A-Za-z0-9]\w+$",
                "description": "Language specification validator for committee approved extensions. In practice target extension should be a static property and this catch all should be removed"
            },
            {
                "pattern": r"^x-[A-Za-z0-9]\w+:[A-Za-z0-9]\w+$",
                "description": "Language specification validator for custom target extensions. In practice target extension should be a static property and this catch all should be removed"
            }
        ]


@definition
class Targets(ArrayOfModel):
    """
    List of Target fields
    """
    valueType = Enumerated(Target)
    minimum = 1
    maximum = 0
    unique = True


@definition
class Action_Targets(MapOfModel):
    """
    Map of each action supported by this actuator to the list of targets applicable to that action
    """
    alias = "Action-Targets"
    keyType = Action
    valueType = Targets


@definition
class Results(MapModel):
    """
    Response Results
    """
    versions = Field(id=1, type=Versions, desc="List of OpenC2 language versions supported by this Actuator")
    profiles = Field(id=2, type=Profiles, desc="List of profiles supported by this Actuator")
    pairs = Field(id=3, type=Action_Targets, desc="List of targets applicable to each supported Action")
    rate_limit = Field(id=4, type=Number(minimum=0), desc="Maximum number of requests per minute supported by design or policy")

    class Options:
        patternProperties = [
            {
                "pattern": rf"^({'|'.join(Valid_Extensions)})$",
                "type": SchemaTypes.Object,
                "description": "Language specification validator for committee approved results extensions. In practice results extension should be a static property and this catch all should be removed",
                "minimum": 1
            },
            {
                "pattern": r"^x-[A-Za-z0-9]\w+$",
                "type": SchemaTypes.Object,
                "description": "Language specification validator for custom results extensions. In practice results extension should be a static property and this catch all should be removed",
                "minimum": 1
            }
        ]


class OpenC2_Language_Objects(SchemaModel):
    """
    OpenC2 Language Specification version 1.0 csprd01
    """
    module = "http://oasis-open.org/openc2/oc2ls/v1.0"
    config = dict(
        FS=":",
        FieldName=r"^(x-|[a-z])[_A-Za-z0-9]{0,31}$"
    )

    @export
    @definition
    class OpenC2_Command(RecordModel):
        """
        The Command defines an Action to be performed on a Target
        """
        action = Field(id=1, type=Action, options=dict(required=True), desc="The task or activity to be performed (i.e., the 'verb')")
        target = Field(id=2, type=Target, options=dict(required=True), desc="The object of the Action. The Action is performed on the Target")
        args = Field(id=3, type=Args, desc="Additional information that applies to the Command")
        actuator = Field(id=4, type=Actuator, desc="The subject of the Action. The Actuator executes the Action on the Target")
        command_id = Field(id=5, type=Command_ID, desc="An identifier of this Command")

        class Options:
            alias = "OpenC2-Command"

    @export
    @definition
    class OpenC2_Response(RecordModel):
        status = Field(id=1, type=Status_Code, options=dict(required=True), desc="An integer status code")
        status_text = Field(id=2, type=String, desc="A free-form human-readable description of the Response status")
        results = Field(id=3, type=Results, desc="Map of key:value pairs that contain additional results based on the invoking Command")

        class Options:
            alias = "OpenC2-Response"
