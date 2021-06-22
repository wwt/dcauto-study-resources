# Data Center Device-Centric Networking

## Overview

This section of the exam topics focuses on the programmability features of the Cisco Nexus series of switches, when the switches run the **Cisco Open NX-OS** operating system.  We found this particular exam topic section has the most technical variety of its counterparts and, thus, required us to build and practice a pretty diverse set of skills in the course of our DCAUTO exam prep.  We spent a good amount of time learning to pay close attention to discreet differences between the many types Open NX-OS programmatic interfaces plus how Open NX-OS models its configuration and state data using its Data Management Engine (DME) and YANG model options (both Native and OpenConfig).

???+ note "Section 3.0 Topic Details"
    - 3.1 Describe Day 0 provisioning with NX-OS
        - 3.1.a Cisco POAP
        - 3.1.b NX-OS iPXE
    - 3.2 Implement On-Box Programmability and Automation with NX-OS
        - 3.2.a Bash
        - 3.2.b Linux containers (LXC and Docker using provided container)
        - 3.2.c NX-OS guest shell
        - 3.2.d Embedded Event Manager (EEM)
        - 3.2.e On-box Python Scripting
    - 3.3 Compare model-driven telemetry such as YANG Push and gRPC to traditional network monitoring strategies such as SMNP, Netflow, and SYSLOG
    - 3.4 Construct Python script that consumes model-driven telemetry data with NX-OS
    - 3.5 Implement Off-Box Programmability and Automation with NX-OS
        - 3.5.a Nexus NX-API (NX-API REST and NX-API CLI)
        - 3.5.b Nexus NETCONF using native and OpenConfig
        - 3.5.c Network configuration tools with NX-OS (Ansible)

---

## Resources

### :material-code-json: Cisco DevNet

??? abstract "Learning Labs"
    - [NX-OS Programmability](https://developer.cisco.com/learning/tracks/nxos-programmability "NX-OS Programmability Learning Path"){target=_blank}
        - **Introduction to NX-OS Programmability Module** - All Labs
        - **NETCONF/YANG on Nexus** - All Labs
        - **Introduction to ACI and Ansible Module** -  All Labs

---

### Videos on Demand

#### :fontawesome-solid-dollar-sign: Pluralsight

??? abstract "Individual Courses"
    - [Cisco Data Center Core: Implementing Automation](https://www.pluralsight.com/courses/cisco-data-center-core-implementing-automation "Cisco Data Center Core: Implementing Automation"){target=_blank}

---

#### :fontawesome-solid-laptop-code: Cisco YouTube

??? abstract "Cisco Live"
    - [Programmability and Automation on Cisco Nexus Platforms - DEVNET-1467](https://www.ciscolive.com/global/on-demand-library.html?#/session/1511296148544001AtHE "Programmability and Automation on Cisco Nexus Platforms - DEVNET-1467"){target=_blank}
    - [Maximizing Network Programmability and Automation with Open NX-OS](https://www.ciscolive.com/global/on-demand-library.html?#/session/1509501635501001PcDT "Maximizing Network Programmability and Automation with Open NX-OS"){target=_blank}
    - [Data Center Telemetry with Nexus and NX-OS](https://www.ciscolive.com/global/on-demand-library.html?#/session/1517500106507001F3Ph "Data Center Telemetry with Nexus and NX-OS"){target=_blank}
    - [NX-OS Automation and Telemetry Made Simple, Powerful and Scalable with Open-Source Tools](https://www.ciscolive.com/global/on-demand-library.html?#/session/1542224312195001r70N "NX-OS Automation and Telemetry Made Simple, Powerful and Scalable with Open-Source Tools"){target=_blank}

---

### :fontawesome-regular-keyboard: Hands-On Learning

??? abstract "DevNet Sandbox Labs"
    - [DevNet Reservable Open NX-OS Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/0e22761d-f813-415d-a557-24fa0e17ab50?diagramType=Topology "DevNet Reservable Open NX-OS Sandbox"){target=_blank}

??? abstract "Development Environment Resources"

    !!! attention
        - The links below require that the local Jupyter Lab server is active and listening on [**http://localhost:8888**](http://localhost:8888 "Jupyter Lab Server"){target=_blank}
            - The Visual Studio Code Development Environment automatically activates the Jupyter Lab server.

        !!! tip
            - You may also use Visual Studio Code to explore the same code samples and hands-on exercises.  The **resources** folder within the Development Environment Container contains all of the source files.
        

    - :material-ansible: [Ansible Files](http://localhost:8888/lab/tree/resources/aci/ansible "Ansible Root Folder"){target=_blank}
        - [Sample Configuration File](http://localhost:8888/lab/workspaces/auto-c/tree/resources/aci/ansible/ansible.cfg "Sample Configuarion File"){target=_blank}
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

    ??? tip "New to Jupyter Lab? Expand This Section for Help"

        ??? example "1. Open the [Jupyter Lab Server](http://localhost:8888 "Jupyter Lab Server"){target=_blank}"

            [![vs-code-open-terminals](../images/vs-code-open-terminals.png "Open New Bash or PowerShell Terminals")](../../images/vs-code-open-terminals.png){target=_blank}

        ??? example "2. Navigate to the **resources/aci** Directory"

            [![vs-code-open-terminals](../images/vs-code-open-terminals.png "Open New Bash or PowerShell Terminals")](../../images/vs-code-open-terminals.png){target=_blank}

        ??? example "3. Open a Jupyter Notebook in Either the **cobra-sdk/exercises** or **rest-api/exercises** Folder"

            [![vs-code-open-terminals](../images/vs-code-open-terminals.png "Open New Bash or PowerShell Terminals")](../../images/vs-code-open-terminals.png){target=_blank}

??? abstract "Management Information Tree (MIT) Assembly Challenge"
    - Review the scrambled, disconnected ACI MIT diagrams in the **resources/aci/mit** folder, within the development environment, and try to draw them (digitally or on paper) in the correct positions with the correct connections.
        - Option #1 - [.png quiz #1](http://localhost:8888/lab/tree/resources/aci/mit/png/quiz_1.png ".png quiz #1"){target=_blank}, [.png quiz #2](http://localhost:8888/lab/tree/resources/aci/mit/png/quiz_1.png ".png quiz #2"){target=_blank}, and [.png solution](http://localhost:8888/lab/tree/resources/aci/mit/png/solution/solution.png ".png solution"){target=_blank}
        - Option #2 -  [Visio Quiz and Solution File](http://localhost:8888/lab/tree/resources/aci/mit/visio/quizzes_and_solution.vsdx "Visio Quiz and Solution File"){target=_blank}

---

## :material-file-document-outline: Documentation

??? abstract "ACI Fundamentals"
    - [ACI Terminology Reference](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/kb/b_ACI_Terminology.html "ACI Terminology Reference"){target=_blank}
    - [ACI Policy Model Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/policy-model-guide/b-Cisco-ACI-Policy-Model-Guide.html "ACI Policy Model Guide"){target=_blank}
        - [ACI Policy Model Quick Reference](https://www.cisco.com/c/dam/en/us/td/i/500001-600000/500001-510000/501001-502000/501289.jpg "ACI Policy Model Quick Reference"){target=_blank}
    - [Cisco DC App Center](https://dcappcenter.cisco.com "Cisco DC App Center"){target=_blank}

??? abstract "ACI Programmability"
    - [APIC REST API Configuration Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/2-x/rest_cfg/2_1_x/b_Cisco_APIC_REST_API_Configuration_Guide.html "APIC REST API Configuration Guide"){target=_blank}
    - [APIC Python SDK Documentation](https://cobra.readthedocs.io/en/latest/ "Cisco APIC Python SDK Documentation"){target=_blank}
    - [Ansible Galaxy ACI Collection](https://galaxy.ansible.com/cisco/aci "Ansible Galaxy ACI Collection"){target=_blank}

??? abstract "ACI Kubernetes CNI Plugin Integration for Red Hat OpenShift"
    - [ACI and Kubernetes Solution Overview](https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/solution-overview-c22-739493.html "ACI and Kubernetes Solution Overview"){target=_blank}
    - [ACI and Kubernetes Architecture and Design Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/white_papers/Cisco-ACI-CNI-Plugin-for-OpenShift-Architecture-and-Design-Guide.html "ACI and Kubernetes Architecture and Design Guide"){target=_blank}
    - [ACI and Kubernetes Integration Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/kb/b_Kubernetes_Integration_with_ACI.html "ACI and Kubernetes Integration Guide"){target=_blank}

---

## :fontawesome-solid-lightbulb: Insights

- Lab resources were hard to find

- Telemetry scripts were tough to find source information for

- Type out all of the NETCONF payloads (you will learn the YANG models better)

- We spent plenty of time watching the videos and reading the documentation in this guide although we spent most of our time going through the hands-on learning exercises over, and over, and over again.  The practice made a big difference in our ability to retain so many details.  Forcing ourselves to type our way through the Jupyter Lab exercises was really hard and was also our best teacher.

- The Cisco DevNet learning labs for ACI were a great starting point for us and set the tone for the things we needed to learn and practice.  Following those up with the Jupyter and MIT exercises was very beneficial.

- The star resource to practice just about any skills related to ACI is the **[DevNet Always-On ACI Sandbox](https://sandboxapicdc.cisco.com "DevNet Always-On ACI Sandbox"){target=_blank}**.  This is a publicly-accessible (no-VPN required), reservationless, read/write, read/write ACI simulator and we used it excessively.  All of the code samples, Jupyter Notebooks, and Ansible Playbooks bundled in this repository use this sandbox.

!!! caution
        - From time to time, the **[DevNet Always-On ACI Sandbox](https://sandboxapicdc.cisco.com "DevNet Always-On ACI Sandbox"){target=_blank}** can be a bit slow or fail to respond to your API call, browser session, etc.  Generally, after a minute or two, we found the sandbox would recover from these situations.

    !!! tip "tips"
        - Spend plenty of time working with ACI both programmatically _and_ in the APIC GUI.
        - The [ACI visore tool](https://www.cisco.com/c/en/us/support/docs/cloud-systems-management/application-policy-infrastructure-controller-apic/118839-technote-visore-00.html "ACI visore tool"){target=_blank} provides a great way to understand relationships between ACI objects in the MIT.
        - The [ACI API Inspector](https://aci-prog-lab.ciscolive.com/lab/pod1/references/find-object "ACI API Inspector"){target=_blank} vastly simplifies the process to construct REST payloads for ACI.  We recommend that you spend plenty of time observing how you can use APIC GUI interactions, via the API Inspector, to construct REST payloads within Python.

## On to Section 4.0

:thumbsup:  You finished going through all of the Open NX-OS resources!  One more section to go, click [this link](section_4.md "Section 4.0") to check out **Section 4.0** exam topics and resources.
