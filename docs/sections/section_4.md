# Data Center Compute

## Overview

This section of the exam topics primarily focuses on the programmability features of the Cisco UCS Platform, including UCSM and [Cisco Intersight](https://www.intersight.com "Cisco Intersight"){target=_blank}.  There are many programmable interfaces for UCS platforms including a Python SDK, Windows PowerShell (via the UCS PowerTool), and a variety of REST APIs.  Our study for this section required that We spent a lot of time in our Visual Studio Code development environment, using the UCS PowerTool CLI, writing Python with the UCS Python SDK, and also writing Python to interact with the Intersight API.

???+ note "Section 4.0 Topic Details"
    - 4.1 Configure Cisco UCS with developer tools
        - 4.1.a UCS PowerTool
        - 4.1.b UCS Python SDK
        - 4.1.c Ansible
    - 4.2 Describe the capabilities of the DCNM API
    - 4.3 Identify the steps in the Intersight API authentication method
    - 4.4 Construct an Intersight API call given documentation to accomplish tasks such as manage server policies, service profiles, and firmware updates
    - 4.5 Describe the process to implement workflows for physical and virtual infrastructure using UCS Director
        - 4.5.a Pre-defined tasks
        - 4.5.b Custom tasks
        - 4.5.c Script libraries
        - 4.6 Utilize UCS Director REST API browser

---

## Resources

### :material-code-json: Cisco DevNet

??? abstract "Learning Labs"
    - [UCS Programmability](https://developer.cisco.com/learning/tracks/ucs-compute-prog "UCS Programmability Learning Path"){target=_blank}
        - **UCS PowerTool Introduction** - All Labs
        - **UCS Python SDK Introduction** - All Labs
        - **UCS PowerTool and UCS Python Intermediate** -  All Labs
        - **Cisco Intersight REST API** - All Labs
    - [UCS for Application Developers](https://developer.cisco.com/learning/tracks/ucsd-resource-automation "UCS for Application Developers Learning Pat"){target=_blank}
        - **UCS Director REST API Introduction** - All Labs

---

### Videos on Demand

#### :fontawesome-solid-laptop-code: Cisco Live

??? abstract "On-Demand Library"
    - [Automating Your Cisco UCS with Python - Managing Your Infrastructure as Code - DEVNET-1611](https://www.ciscolive.com/global/on-demand-library.html#/session/1510617043449001nob5 "Automating Your Cisco UCS with Python - Managing Your Infrastructure as Code - DEVNET-1611"){target=_blank}
    - [Cisco UCS & Cisco Intersight - Programmability Automation & Orchestration Overview - DGTL-BRKPRG-2432](https://www.ciscolive.com/global/on-demand-library.html#/session/1573153551744001JcLV "Cisco UCS & Cisco Intersight - Programmability Automation & Orchestration Overview - DGTL-BRKPRG-2432"){target=_blank}
    - [Creating, Distributing, Maintaining and Utilizing the Cisco Intersight and Cisco UCS Ansible Collections - DGTL-DEVNET-2700](https://www.ciscolive.com/global/on-demand-library.html#/session/1582806029472001wWax "Creating, Distributing, Maintaining and Utilizing the Cisco Intersight and Cisco UCS Ansible Collections - DGTL-DEVNET-2700"){target=_blank}
    - [UCS Manager Automation with Ansible - DEVNET-1586](https://www.ciscolive.com/global/on-demand-library.html#/session/1542224338659001rvdb "UCS Manager Automation with Ansible - DEVNET-1586"){target=_blank}
    - [Cisco UCS PowerTool - Deploy at Scale - DEVNET-2562](https://www.ciscolive.com/global/on-demand-library.html#/session/1542224343090001rMoa "Cisco UCS PowerTool - Deploy at Scale - DEVNET-2562"){target=_blank}

---

### :fontawesome-regular-keyboard: Hands-On Learning

??? abstract "DevNet Sandbox Labs"
    - [DevNet UCS Management Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/3323b7b0-b70b-4b1e-a929-6bdbff3aac8a?diagramType=Topology "DevNet UCS Management Sandbox"){target=_blank}
    - [UCS Platform Emulator](https://community.cisco.com/t5/unified-computing-system/ucs-platform-emulator-downloads-ucspe-4-1-2cpe1-ucspe-4-0-4epe1/ta-p/3648177 "UCS Platform Emulator"){target=_blank}
    - [DevNet Cisco Intersight Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/a63216d2-e891-4856-9f27-309ca61ec862?diagramType=Topology "DevNet Cisco Intersight Sandbox"){target=_blank}
    - [Intersight Managed Object Browser](https://intersight.com/mobrowser "Intersight Managed Object Browser"){target=_blank}

??? abstract "Development Environment Resources"

    !!! attention
        - The links below require that the local Jupyter Lab server is active and listening on [**http://localhost:8888**](http://localhost:8888 "Jupyter Lab Server"){target=_blank}
            - The Visual Studio Code Development Environment automatically activates the Jupyter Lab server.

        !!! question "New to Jupyter Lab? [Click Here for an Overview](appendix_b.md "Jupyter Lab Overview"){target=_blank}"

        !!! tip
            - You may also use Visual Studio Code to explore the same code samples and hands-on exercises.  The **resources** folder within the Development Environment Container contains all of the source files.

        - :material-ansible: [Ansible Files](http://localhost:8888/lab/tree/resources/ucs/ansible "Ansible Root Folder"){target=_blank}
            - [Sample Configuration File](http://localhost:8888/lab/workspaces/auto-c/tree/resources/ucs/ansible/ansible.cfg "Sample Configuration File"){target=_blank}
            - [Sample Playbook 1](http://localhost:8888/lab/workspaces/auto-c/tree/resources/ucs/ansible/ucspe_test.yml "Sample Playbook 1"){target=_blank}
            - [Sample Inventory File (.ini format)](http://localhost:8888/lab/workspaces/auto-c/tree/resources/ucs/ansible/inventory/hosts.ini "Sample Inventory File (.ini format)"){target=_blank}

        ---

        - :fontawesome-brands-python: [UCS Python SDK Examples](http://localhost:8888/lab/workspaces/auto-I/tree/resources/ucs/ucsm/python_sdk_examples.ipynb "UCS Python SDK Examples"){target=_blank}

        ---

        - :material-api: [Intersight REST API](http://localhost:8888/lab/tree/resources/ucs/intersight "Intersight REST API"){target=_blank}

        ??? danger "Important Intersight Code Usage Notes"
            Cisco Intersight REST API keys require an HTTP signature, and the initial setup of Intersight authentication requires several manual steps.  This repository already includes the [Intersight Authentication Repository](https://github.com/movinalot/intersight-rest-api "Intersight Authentication Repository") files recommended by Cisco DevNet.  These files provide the functionality required to support Intersight authentication via Python.

            If you would like to use the Intersight Python code and Jupyter Notebook examples, you must first perform the following steps:

            1. Obtain Intersight `keyId` and `keySecret` data using the [Intersight API Authorization](https://intersight.com/apidocs/introduction/security/#benefits-of-using-api-keys "Intersight API Authorization") instructions.
            2. Create new blank text files within your local copy of the **dcauto-study-resources** repository with the paths:

                - `/resources/ucs/intersight/api_keys/keyId.txt`
                - `/resources/ucs/intersight/api_keys/keySecret.txt`

            3. Paste the contents of your Intersight `keyId` into the `keyId.txt` file.

            ??? abstract "`keyId.txt` example file contents"
                4196c31c7562012c339be0b/6129f1c7564612d331be0fd/6096c3552128512d339be2cb

            4. Paste the contents of your Intersight `keySecret` into the `keySecret.txt` file.

            ??? abstract "`keySecret.txt` example file contents"
                -----BEGIN RSA PRIVATE KEY-----
                WuJ1V54N4uHj9rjDRvl9zp2eoA0J6SFB+dwp2Hoj24+pSnr4FPJ/9+PgcRsgUVjq
                IEHbVKRnrr2xWcXtQnUsa0Dxbdw8biyoo2UiHlCyxUqJEtzSEeeWf9V8hjyqUwtr
                UyIeWZOhQ2NYbboUgrCMeHhgE6LNTbrGAaSmNZ3BSJnPvRCM7u5xRkFvAoGBAPcN
                skfHYw23WHTTZD/Z1m1kYZj2LkgAI3/LDQNHaE/enxvq0q+/SrrSVraYBhp8B7xO
                Vg7gbMXRczSCh5jhQqMm5K1I8ZBlWG0kNdQcuuabAGewNr7bRc+LVZQN+RKsQ8BJ
                /00bV3GmkD30YYF7pS6LrDiErvYudS0C+9NYeMXgST1OTnRh+YVNisBwvS02Gbyc
                Uv+Eiy2ZnsIxDiqlvWlGlIrMeLiwmPDVeoM0XyfkZ+5DLFKQYFYABf7LFQuWaKfw
                LndthGB60BM2nZXohSJzgPsCgYEAi2zlYnD6S/FfMH9kokxUIWR3WBYHRIcfga2c
                aG9SRVEERoMd6CVzDUBLw7zEJQo+a11iX/70JCfydn37/KGUM/NtNwZlnfI0F1RK
                NK0KJb7wWZQvMUMagOjHoUjJempRyiEDJpm96VxMWCotG/likj052PxdctvHsRg8
                Ad0L3K0CgYAgmXD6dUCJqDOwfs9BBbD6bbr6aE7kitLEoOZ0Rz37MSmenJMt6/mf
                tIuV+MMhHKWxXtLCUPZjP60nk/d2oR6tN7X75QL9ioduN/QIArZGog==
                -----END RSA PRIVATE KEY-----

        - [Intersight API Python Helper Functions](http://localhost:8888/lab/tree/resources/ucs/intersight/intersight_helper.py "Intersight API Python Helper Functions"){target=_blank}
            - The docstrings in `intersight_helper.py` include usage instructions.
            - Use these helper functions from your Python interpreter/REPL with the expression:
                - `from intersight_helper import *`

??? abstract "UCS Director REST API Notes"

    - API endpoint to request an API key:
        - `https://{{ucsd}}/app/api/rest?opName=getRESTKey&user={{username}}&password={{password}}`
    - Authentication header name:
        - `X-Cloupia-Request-Key`
    - Possible query parameters:
        - `opName` - name of the current operation.
        - `opData`- payload body.
        - `formatType` - json (default) or xml.

??? abstract "DCNM REST API Notes"

    - DCNM has Multiple APIs:
        - LAN Fabric.
        - L4-L7 Services.
        - Endpoint Locator.
        - Media Controller (DCNM control plane).
        - SAN Management.

    - APIs support `GET`, `POST`, `PUT`, & `DELETE` operations.
    - API Authentication:
        - API URI Endpoint - `/logon`
        - Authentication mechanism - **HTTP Basic**
            - Successful authentication requests return a token which must be sent in subsequent API requests, in a custom header with the format:
                - `{"DCNM-Token": token}`

---

## :material-file-document-outline: Documentation

??? abstract "UCS Developer Tools"
    - [UCS Python SDK Reference Guide](hhttps://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk_ug.html "UCS Python SDK Reference Guide"){target=_blank}
    - [UCS PowerTool Resource Landing Page](https://community.cisco.com/t5/cisco-developed-ucs-integrations/cisco-ucs-powertool-suite-powershell-modules-for-cisco-ucs/ta-p/3639523 "UCS PowerTool Resource Landing Page"){target=_blank}
    - [DevNet UCS PowerTool Docker Container on Docker Hub](https://hub.docker.com/r/ciscodevnet/ucs-powertool-core-ms "DevNet UCS PowerTool Docker Container on Docker Hub"){target=_blank}
        - The resources in this Docker Container are already built-in to the Visual Studio Development Container in this repository.

??? abstract "Cisco Intersight Programmability"
    - [Cisco Intersight RESTful API Guide](https://intersight.com/apidocs/introduction/overview/ "Cisco Intersight RESTful API"){target=_blank}

??? abstract "Ansible with UCS and Intersight"
    - [Ansible Galaxy UCS Manager Collection](https://galaxy.ansible.com/cisco/ucs "Ansible Galaxy UCS Manager Collection"){target=_blank}
    - [Ansible Galaxy Intersight Collection](https://galaxy.ansible.com/cisco/intersight "Ansible Galaxy Intersight Collection"){target=_blank}

??? abstract "UCS Director and DCNM"
    - [Cisco UCS Director REST API Getting Started Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-director/rest-api-getting-started-guide/6-5/cisco-ucs-director-REST-API-getting-started-65.html "Cisco UCS Director REST API Getting Started Guide"){target=_blank}
    - [Cisco UCS Director Orchestration Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-director/orchestration-guide/6-8/cisco-ucs-director-orchestration-68.html "Cisco UCS Director Orchestration Guide"){target=_blank}

---

## :fontawesome-solid-lightbulb: Insights

- We spent plenty of time watching the videos and reading the documentation in this guide, although we spent most of our time going through the hands-on learning exercises over, and over, and over again.  The practice made a big difference in our ability to retain so many details.  Forcing ourselves to type our way through the Jupyter Lab exercises was really hard and was also our best teacher.

- The Cisco DevNet learning labs for ACI were a great starting point for us and set the tone for the things we needed to learn and practice.  Following those up with the Jupyter and MIT exercises was very beneficial.

- The star resource to practice just about any skills related to ACI is the **[DevNet Always-On ACI Sandbox](https://sandboxapicdc.cisco.com "DevNet Always-On ACI Sandbox"){target=_blank}**.  This is a publicly accessible (no-VPN required), reservation-less, read/write, read/write ACI simulator, and we used it excessively.  All of the code samples, Jupyter Notebooks, and Ansible Playbooks bundled in this repository use this sandbox.

## Lessons Learned

:thumbsup:  You finished the UCS section!  That's all of the study resources we accumulated during our exam preparation.  If you're interested in some general guidance on your path to DCAUTO certification, click [this link](appendix_a.md "Appendix A") to check out a summary of our **Lessons Learned**.

--8<-- "includes/glossary.txt"
