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

??? abstract "Development Environment Resources"
    !!! attention
        - The links below require that the local Jupyter Lab server is active and listening on [**http://localhost:8888**](http://localhost:8888 "Jupyter Lab Server"){target=_blank}
            - The Visual Studio Code Development Environment automatically activates the Jupyter Lab server.

        !!! question "New to Jupyter Lab? [Click Here for an Overview](appendix_b.md "Jupyter Lab Overview"){target=_blank}"

        !!! tip
            - You may also use Visual Studio Code to explore the same code samples and hands-on exercises.  The **resources** folder within the Development Environment Container contains all of the source files.
        

    - :material-ansible: [Ansible Files](http://localhost:8888/lab/tree/resources/aci/ansible "Ansible Root Folder"){target=_blank}
        - [Sample Configuration File](http://localhost:8888/lab/workspaces/auto-c/tree/resources/aci/ansible/ansible.cfg "Sample Configuration File"){target=_blank}
        - [Sample Playbook 1](http://localhost:8888/lab/workspaces/auto-c/tree/resources/aci/ansible/create_aci_tenant_and_children.yml "Sample Playbook 1"){target=_blank}
        - [Sample Playbook 2](http://localhost:8888/lab/workspaces/auto-c/tree/resources/aci/ansible/delete_aci_tenant_and_children.yml "Sample Playbooks 2"){target=_blank}
        - [Sample Playbook 3](http://localhost:8888/lab/workspaces/auto-c/tree/resources/aci/ansible/get_tenant.yml "Sample Playbooks 3"){target=_blank}
        - [Sample Inventory File (.ini format)](http://localhost:8888/lab/workspaces/auto-c/tree/resources/aci/ansible/inventory/hosts.ini "Sample Inventory File (.ini format)"){target=_blank}
        - [Sample Inventory File (.yml format)](http://localhost:8888/lab/workspaces/auto-c/tree/resources/aci/ansible/inventory/hosts.yml "Sample Inventory File (.yml format)"){target=_blank}
        - [Sample Host Variables File](http://localhost:8888/lab/workspaces/auto-c/tree/resources/aci/ansible/inventory/host_vars/sandboxapicdc.cisco.com.yml "Sample Host Variables File"){target=_blank}
    - :fontawesome-brands-python: [ACI Python (Cobra) SDK](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/cobra-sdk "ACI Python (Cobra) SDK"){target=_blank}
        - [Practice Exercise](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/cobra-sdk/exercises/apic_cobra_sdk_exercises.ipynb "Practice Exercise"){target=_blank}
        - [Practice Exercise Solution](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/cobra-sdk/exercises/solutions/apic_cobra_sdk_exercise_solution.ipynb "Practice Exercise Solution"){target=_blank}
        - [Practice Exercise Example](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/cobra-sdk/exercises/examples/apic_cobra_sdk_exercises_example_1.ipynb "Practice Exercise Example"){target=_blank}
    - :material-api: [ACI REST API](http://localhost:8888/lab/tree/resources/aci/rest-api "ACI REST API"){target=_blank}
        - [Practice Exercise](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/rest-api/exercises/apic_rest_exercises.ipynb "Practice Exercise"){target=_blank}
        - [Practice Exercise Solution](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/rest-api/exercises/solutions/apic_rest_exercise_solution.ipynb "Practice Exercise Solution"){target=_blank}
        - [Practice Exercise Example #1](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/rest-api/exercises/examples/apic_rest_exercises_example_1.ipynb "Practice Exercise Example #1"){target=_blank}
        - [Practice Exercise Example #2](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/rest-api/exercises/examples/apic_rest_exercises_example_2.ipynb "Practice Exercise Example #2"){target=_blank}
        - [Python Code Samples](http://localhost:8888/lab/workspaces/auto-I/tree/resources/aci/rest-api/code-samples "Python Code Samples"){target=_blank}

??? abstract "Management Information Tree (MIT) Assembly Challenge"
    - Review the scrambled, disconnected ACI MIT diagrams in the **resources/aci/mit** folder within the development environment, and try to draw them (digitally or on paper) in the correct positions with the proper connections.
        - Option #1 - [.png quiz #1](http://localhost:8888/lab/tree/resources/aci/mit/png/quiz_1.png ".png quiz #1"){target=_blank}, [.png quiz #2](http://localhost:8888/lab/tree/resources/aci/mit/png/quiz_1.png ".png quiz #2"){target=_blank}, and [.png solution](http://localhost:8888/lab/tree/resources/aci/mit/png/solution/solution.png ".png solution"){target=_blank}
        - Option #2 -  [Visio Quiz and Solution File](http://localhost:8888/lab/tree/resources/aci/mit/visio/quizzes_and_solution.vsdx "Visio Quiz and Solution File"){target=_blank}

---

## :material-file-document-outline: Documentation

??? abstract "UCS Developer Tools"
    - [ACI Terminology Reference](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/kb/b_ACI_Terminology.html "ACI Terminology Reference"){target=_blank}

??? abstract "Cisco Intersight Programmability"
    - [APIC REST API Configuration Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/2-x/rest_cfg/2_1_x/b_Cisco_APIC_REST_API_Configuration_Guide.html "APIC REST API Configuration Guide"){target=_blank}

??? abstract "UCS Director and DCNM"
    - [ACI and Kubernetes Solution Overview](https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/solution-overview-c22-739493.html "ACI and Kubernetes Solution Overview"){target=_blank}

---

## :fontawesome-solid-lightbulb: Insights

- We spent plenty of time watching the videos and reading the documentation in this guide, although we spent most of our time going through the hands-on learning exercises over, and over, and over again.  The practice made a big difference in our ability to retain so many details.  Forcing ourselves to type our way through the Jupyter Lab exercises was really hard and was also our best teacher.

- The Cisco DevNet learning labs for ACI were a great starting point for us and set the tone for the things we needed to learn and practice.  Following those up with the Jupyter and MIT exercises was very beneficial.

- The star resource to practice just about any skills related to ACI is the **[DevNet Always-On ACI Sandbox](https://sandboxapicdc.cisco.com "DevNet Always-On ACI Sandbox"){target=_blank}**.  This is a publicly accessible (no-VPN required), reservation-less, read/write, read/write ACI simulator, and we used it excessively.  All of the code samples, Jupyter Notebooks, and Ansible Playbooks bundled in this repository use this sandbox.

!!! caution
        - From time to time, the **[DevNet Always-On ACI Sandbox](https://sandboxapicdc.cisco.com "DevNet Always-On ACI Sandbox"){target=_blank}** can be a bit slow or fail to respond to your API call, browser session, etc.  Generally, after a minute or two, we found the sandbox would recover from these situations.

    !!! tip "tips"
        - Spend plenty of time working with ACI both programmatically _and_ in the APIC GUI.
        - The [ACI visore tool](https://www.cisco.com/c/en/us/support/docs/cloud-systems-management/application-policy-infrastructure-controller-apic/118839-technote-visore-00.html "ACI visore tool"){target=_blank} provides a great way to understand relationships between ACI objects in the MIT.
        - The [ACI API Inspector](https://aci-prog-lab.ciscolive.com/lab/pod1/references/find-object "ACI API Inspector"){target=_blank} vastly simplifies the process to construct REST payloads for ACI.  We recommend that you spend plenty of time observing how you can use APIC GUI interactions, via the API Inspector, to build REST payloads within Python.

## Lessons Learned

:thumbsup:  You finished the UCS section!  That's all of the study resources we accumulated during our exam preparation.  If you're interested in some general guidance on your path to DCAUTO certification, click [this link](appendix_a.md "Appendix A") to check out a summary of our **Lessons Learned**.

--8<-- "includes/glossary.txt"
