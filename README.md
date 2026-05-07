[![License](https://img.shields.io/badge/license-Apache_2.0-brightgreen.svg)](https://github.com/arista-netdevops-community/cloudvision-automation/blob/master/LICENSE)
[![CI](https://github.com/arista-netdevops-community/cloudvision-automation/actions/workflows/test.yml/badge.svg)](https://github.com/arista-netdevops-community/cloudvision-automation/actions)

**Table of Contents**

- [About this repository](#about-this-repository)
- [About the tools used in this repository](#about-the-tools-used-in-this-repository)
- [Requirements](#requirements)
- [CVP version](#cvp-version)
- [Credits](#credits)

# About this repository

This repository has CloudVision automation examples

- [GO](GO.md): How to install GO which is a requirement to install some tools
  - gRPCurl
- [Token based authentication](token_based_authentication/): How to configure token based authentication which is a requirement in order to use CVP APIs
- [REST APIs](REST_APIs/): How to use REST APIs with
  - cURL
  - Wget
  - Python with the module requests
- [OpenAPI](OpenAPI): How to use the OpenAPI file that describe the CVP REST APIs with
  - Postman
  - Online swagger editor
- [Resource APIs](resource_APIs/): How to use resources API with
  - cURL
  - Python with the module
    - requests
    - cvprac
  - gRPCurl
  - Postman
- [cvprac](cvprac/): How to use the Python module cvprac
- [Certificate based authentication](certificate_based_authentication): How to configure certificate based authentication (for the devices and CVP communication)
  - gRPCurl
  - Postman
- [RESTCONF](RESTCONF/): How to use RESTCONF with
  - cURL
  - Python with the module requests

# About the tools used in this repository

- **cURL** is a command-line tool for getting or sending data using URLs
- **Wget** is a program that retrieves content from web servers
- **Postman** can be used to explore and test REST APIs and gRPC services
- **Python** with the following modules:
  - The **requests** library can be used for making HTTP requests in Python
  - The **cvprac** python library can be used to manage CVP. cvprac is written using CVP REST APIs an CVP resource APIs


# Requirements

- CVP APIs require [token based authentication](Token_based_authentication).  
  
# CVP version

All examples in this repository have been tested with CVP version 2022.1.0.

# Credits

Thank you to [Angélique Phillipps](https://github.com/aphillipps), [Khelil Sator](https://github.com/ksator), [Matthieu Tache](https://github.com/mtache) and [Tamas Plugor](https://github.com/noredistribution) for their contributions and guidances.
