# Under Construction - Data Center Device-Centric Networking

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

---

## :material-file-document-outline: Documentation

---

## :fontawesome-solid-lightbulb: Insights

- Lab resources were hard to find.

- It was difficult to find documentation to construct Python scripts which consume MDT.

- Type out all of the NETCONF payloads in the DevNet labs (you will learn the YANG models better)

## On to Section 4.0

:thumbsup:  You finished going through all of the Open NX-OS resources!  One more section to go, click [this link](section_4.md "Section 4.0") to check out **Section 4.0** exam topics and resources.
