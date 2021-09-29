# Data Center Device-Centric Networking

## Overview

This section of the exam topics focuses on the programmability features of the Cisco Nexus series of switches, when the switches run the **Cisco Open NX-OS** operating system.  We found this particular exam topic section has the most technical variety of its counterparts and, thus, required us to build and practice a pretty diverse set of skills in the course of our DCAUTO exam prep.  We spent a good amount of time learning to pay close attention to discreet differences between the many types of Open NX-OS programmatic interfaces plus how Open NX-OS models its configuration and state data using its Data Management Engine (DME) and YANG model options (both Native and OpenConfig).

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

??? abstract "Files and Scripts"
    - [NX-OS OpenConfig YANG Model RPM Artifactory](https://devhub.cisco.com/artifactory/open-nxos-agents/ "NX-OS OpenConfig YANG Model RPM Artifactory"){target=_blank}
    - [NX-OS POAP Python Script - GitHub Repository](https://github.com/datacenter/nexus9000/blob/master/nx-os/poap/poap.py "NX-OS POAP Python Script - GitHub Repository"){target=_blank}
    - [NX-OS gRPC Telemetry Protocol Definitions - GitHub Repository](https://github.com/CiscoDevNet/nx-telemetry-proto "NX-OS gRPC Telemetry Protocol Definitions - GitHub Repository"){target=_blank}

---

### Videos on Demand

#### :fontawesome-solid-laptop-code: Cisco Live

??? abstract "On-Demand Library"
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

        !!! question "New to Jupyter Lab? [Click Here for an Overview](appendix_b.md "Jupyter Lab Overview"){target=_blank}"

        !!! tip
            - You may also use Visual Studio Code to explore the same code samples and hands-on exercises.  The **resources** folder within the Development Environment Container contains all of the source files.
        
    - :material-ansible: [Ansible Files](http://localhost:8888/lab/tree/resources/nexus/ansible "Ansible Root Folder"){target=_blank}
        - [Sample Configuration File](http://localhost:8888/lab/workspaces/auto-c/tree/resources/nexus/ansible/ansible.cfg "Sample Configuration File"){target=_blank}
        - [Sample Playbook 1](http://localhost:8888/lab/workspaces/auto-c/tree/resources/nexus/ansible/setup_nxos_docker.yml "Sample Playbook 1"){target=_blank}
        - [Sample Playbook 2](http://localhost:8888/lab/workspaces/auto-c/tree/resources/nexus/ansible/upgrade_nxos_software.yml "Sample Playbooks 2"){target=_blank}
        - [Sample Inventory File (.yml format)](http://localhost:8888/lab/workspaces/auto-c/tree/resources/nexus/ansible/inventory/hosts.yml "Sample Inventory File (.yml format)"){target=_blank}
        - [Sample Host Variables File](http://localhost:8888/lab/workspaces/auto-c/tree/resources/nexus/ansible/host_vars/n9kv.yml "Sample Host Variables File"){target=_blank}
        - [Sample Group Variables File](http://localhost:8888/lab/workspaces/auto-c/tree/resources/nexus/ansible/group_vars/all.yml "Sample Host Variables File"){target=_blank}
    - :fontawesome-brands-python: [gNMI Telemetry Files](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/gnmi "gNMI Telemetry Files"){target=_blank}
        - [gNMI Telemetry Subscription Walk-Through Exercises](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/gnmi/gnmi_dial_in.ipynb "gNMI Telemetry Subscription Walk-Through"){target=_blank}
        - [gNMI Telemetry Subscription Python Code](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/gnmi/gnmi.py "gNMI Telemetry Subscription Python Code"){target=_blank}
        - [gNMI Sample Certificate](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/gnmi/gnmi.pem "gNMI Sample Certificate"){target=_blank}
    - :material-api: [NETCONF](http://localhost:8888/lab/tree/resources/nexus/netconf "NETCONF"){target=_blank}
        - [DevNet Learning Lab Hands-On Exercise](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/netconf/devnet_learning_lab_hands_on/nx_os_ncclient_devnet_lab_hands_on.ipynb "DevNet Learning Lab Hands-On Exercise"){target=_blank}
        - [DevNet Learning Lab Hands-On Exercise Solution](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/netconf/devnet_learning_lab_hands_on/solutions/nx_os_ncclient_devnet_lab_hands_on_solution.ipynb "DevNet Learning Lab Hands-On Exercise Solution"){target=_blank}
        - [NETCONF Walk-Through Exercise](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/netconf/netconf_practice_walkthrough/netconf_practice_walkthrough.ipynb "NETCONF Walk-Through Exercise"){target=_blank}
        - [NETCONF Walk-Through Exercise XML Payloads](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/netconf/netconf_practice_walkthrough/netconf_payloads "NETCONF Walk-Through Exercise XML Payloads"){target=_blank}

??? abstract "WWT On-Demand Labs"
    - [Cisco Ansible Automation Lab](https://www.wwt.com/lab/cisco-ansible-automation-training-lab "WCisco Ansible Automation Lab"){target=_blank}
        - We did not follow the provided lab guide, although you may certainly do so if you are new to Ansible or want some Ansible practice.
        - We used this lab primarily because it contains an NX-OS switch that we could configure to suit our study needs.

---

## :material-file-document-outline: Documentation

??? abstract "Day 0 Provisioning"
    - [iPXE - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_01001.html "iPXE - NX-OS Programmability Guide"){target=_blank}
    - [POAP - NX-OS Configuration Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/fundamentals/configuration/guide/b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x/b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x_chapter_0100.html "POAP - NX-OS Configuration Guide"){target=_blank}

??? abstract "On-Box Programmability and Automation"
    - [Bash - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0101100.html "Bash - NX-OS Programmability Guide"){target=_blank}
    - [Docker on NX-OS - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0100001.html "Docker on NX-OS - NX-OS Programmability Guide"){target=_blank}
    - [Guest Shell - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0100.html "Guest Shell - NX-OS Programmability Guide"){target=_blank}
    - [Embedded Event Manager (EEM) Configuration - NX-OS Configuration Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/system-management/b-cisco-nexus-9000-series-nx-os-system-management-configuration-guide-93x/b-cisco-nexus-9000-series-nx-os-system-management-configuration-guide-93x_chapter_0100010.html "Embedded Event Manager (EEM) Configuration - NX-OS Configuration Guide"){target=_blank}
    - [Embedded Event Manager (EEM) Examples - NX-OS Configuration Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/system-management/b-cisco-nexus-9000-series-nx-os-system-management-configuration-guide-93x/b-cisco-nexus-9000-series-nx-os-system-management-configuration-guide-93x_appendix_011101.html "Embedded Event Manager (EEM) Examples - NX-OS Configuration Guide"){target=_blank}
    - [On-Box Python Scripting - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0110000.html "On-Box Python Scripting - NX-OS Programmability Guide"){target=_blank}

??? abstract "Model-Driven Programmability & Telemetry"
    - [Infrastructure Overview - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_010111.html "Infrastructure Overview - NX-OS Programmability Guide"){target=_blank}
    - [Managing Components - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_011000.html "Managing Components - NX-OS Programmability Guide"){target=_blank}
    - [OpenConfig YANG - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_011001.html "OpenConfig YANG - NX-OS Programmability Guide"){target=_blank}
    - [NETCONF Agent - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0100110.html "NETCONF Agent - NX-OS Programmability Guide"){target=_blank}
    - [XMLIN Tool - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_011011.html "XMLIN Tool - NX-OS Programmability Guide"){target=_blank}
    - [gRPC Agent - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0101111.html "gRPC Agent - NX-OS Programmability Guide"){target=_blank}
    - [gNMI Interface - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0110001.html "gNMI Interface - NX-OS Programmability Guide"){target=_blank}
    - [Model-Driven Telemetry - NX-OS Programmability Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0101001.html "Model-Driven Telemetry - NX-OS Programmability Guide"){target=_blank}

??? abstract "Consuming Model-Driven Telemetry with Python"
    - [Nexus Telemetry with gNMI & OpenConfig White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-744191.html "Nexus Telemetry with gNMI & OpenConfig White Paper"){target=_blank}
    - [Nexus Telemetry with NETCONF & gNMI Blog](https://blogs.cisco.com/datacenter/telemetry-in-action-netconf-and-gnmi-with-a-custom-built-collector "Nexus Telemetry with NETCONF & gNMI Blog"){target=_blank}
    - [Cisco gNMI Python Library - GitHub Repository](https://github.com/cisco-ie/cisco-gnmi-python "Cisco gNMI Python Library - GitHub Repository"){target=_blank}

??? abstract "NX-API"
    - [NX-OS Data Management Engine (DME) Model Reference](https://developer.cisco.com/site/nxapi-dme-model-reference-api/?version=9.3(5) "NX-OS Data Management Engine (DME) Model Reference"){target=_blank}
    - [NX-API CLI](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_010011.html "NX-API CLI"){target=_blank}
    - [NX-API REST](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0101110.html "NX-API REST"){target=_blank}
    - [NX-API Developer Sandbox](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_010110.html "NX-API Developer Sandbox"){target=_blank}

??? abstract "Ansible with NX-OS"
    - [Ansible Galaxy NX-OS Collection](https://galaxy.ansible.com/cisco/nxos "Ansible Galaxy NX-OS Collection"){target=_blank}
    - [Ansible Playbook Examples - GitHub Repository](https://github.com/datacenter/Ansible-NXOS "Ansible Playbook Examples - GitHub Repository"){target=_blank}

??? abstract "General NX-OS Programmability References"
    - [NX-OS Programmability Guide - Platform Documentation](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x.html "NX-OS Programmability Guide - Platform Documentation"){target=_blank}
    - [Open NX-OS Programmability - DevNet Documentation](https://developer.cisco.com/docs/nx-os/ "Open NX-OS Programmability - DevNet Documentation"){target=_blank}

---

## :fontawesome-solid-lightbulb: Insights

- Cisco documentation was our predominant resource for this exam topic section.  We absolutely did **NOT** arbitrarily insert every link from the NX-OS Programmability Guide into this page, just to fill space.  There were only a few DevNet Learning Labs available which address the NX-OS exam topics, so we had to rely heavily on tediously walking through commands and configuration examples in official Cisco documentation.  We **highly** recommend that you invest a lot of hands-on time with the examples in Cisco NX-OS documentation.

- Effective NX-OS hands-on lab resources were hard for us to find.  The lone DevNet NX-OS Sandbox was helpful, although it had some limitations that kept us from practicing certain things, like deploying Docker Containers on NX-OS and configuring POAP.  The WWT Ansible Automation Lab was a good resource for studying and testing Ansible and Docker with NX-OS.  DevNet provides a [Vagrant configuration](https://developer.cisco.com/docs/nx-os/#!developer-tooling/vagrant "DevNet NX-OS Vagrant Configuration"){target=_blank} that we did not use, although it is another NX-OS hands-on resource option.

- We did not find documentation that explicitly showed us how to construct Python scripts that consume model-driven telemetry.  Instead, we pieced together many different resources (referenced in the **Documentation** section) and conducted a lot of trial-and-error testing in order to meet our interpretation of the exam topic intent successfully.  For some really good practice, we recommend that you work through the [gNMI Jupyter Walk-Through](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/gnmi/gnmi_dial_in.ipynb "gNMI Telemetry Subscription Walk-Through"){target=_blank} and [sample Python code](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/gnmi/gnmi.py "gNMI Telemetry Subscription Python Code"){target=_blank} we put together and then write your own code to consume telemetry from different XPaths.

- Something we found very beneficial to our comfort level with NETCONF and YANG models was to go through the DevNet Learning Labs on those topics and, instead of copying and pasting commands (into an NX-OS hands-on environment) or even typing out the NETCONF XML payload examples in the lab guides, we forced ourselves to look at the XPath examples and then try to **manually** type out/construct the XML payloads.  This practice helped us become _much_ more comfortable with YANG models, XML, and NETCONF, in general.  The [NETCONF Jupyter Notebook](http://localhost:8888/lab/workspaces/auto-I/tree/resources/nexus/netconf/netconf_practice_walkthrough/netconf_practice_walkthrough.ipynb "NETCONF Walk-Through Exercise"){target=_blank} we put together was an excellent resource for us to get that practice because the interactivity of Jupyter makes it fast and easy to try something, see it not work, make a change, and try again.

## On to Section 4.0

:thumbsup:  You finished going through all of the Open NX-OS resources!  One more section to go, click [this link](section_4.md "Section 4.0") to check out **Section 4.0** exam topics and resources.

--8<-- "includes/glossary.txt"
