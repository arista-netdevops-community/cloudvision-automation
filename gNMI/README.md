**Table of Contents**

- [About gNMI](#about-gnmi)
- [gNMI and EOS Switches](#gnmi-and-eos-switches)

# About gNMI

gNMI stands for gRPC Network Management Interface.

gNMI specifications are defined in this [repository](https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md)

The gNMI proto file is [here](https://github.com/openconfig/gnmi/blob/master/proto/gnmi/gnmi.proto)  

gNMI is the gRPC service. The Remote Procedure Calls (RPC)  methods of the gNMI service are:

- CAPABILITIES: to discover the capabilities of the target
- SET: to modify the state of the target
- GET: to retrieve snapshots from the target for a specified set of paths
- SUBSCRIBE: to subscribe to updates from the target for a specified set of paths.
  
# gNMI and EOS Switches

EOS supports the 4 gNMI RPCs described above.

The target is a network device. The gNMI server runs on the target.

The gNMI client, typically in a collector or in a network management system, sends the RPCs to the targets to modify and collect data.

Examples:

- https://github.com/arista-netdevops-community/gnmi_demo_with_arista_eos
- https://github.com/arista-netdevops-community/automation_and_telemetry_demo

Refer to the [YANG](../YANG/) lab to understand how to generate paths and trees from YANG modules.

## Examples

You will find in this directory examples using:

- The gNMI command-line client:
  - **gNMIc**
  - **gnmi**
  - **pygnmicli**
- The **pyGNMI** Python library
- The **gRPCurl** command line tool
- **Postman** using gPRC
