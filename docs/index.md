# Cisco DCAUTO Exam Study Resources

## About

:mortar_board: We have many people to thank for helping us pass the Cisco DCAUTO exam.  We have never met many of those people and, likely, will never meet, in-person or otherwise.  Each of these people took time from their lives to publish something they know or built, so the rest of us, somehow, via some search engine, could have even a slightly more straightforward path to whatever it is we want to learn.

:sunrise_over_mountains: To everyone who took the time to help the entire DevNet community, this guide is both nod of appreciation to you and also our way of paying it forward to the next person or people who, like us, feel like climbing to the top of the mountain, however strenuous, is worth the view.  It would be disingenuous for us to make the climb using the ropes people left for us without leaving our own ropes to help the people who follow.  We wish you success in your climb.

---

## Overview

:clipboard: This guide provides content and references which will help you study and prepare yourself for the [**Cisco 300-635 DCAUTO Exam: Automating and Programming Cisco Data Center Solutions**](https://www.cisco.com/c/en/us/training-events/training-certifications/exams/current-list/dcauto-300-635.html "Cisco DCAUTO (300-635) Exam"){target=_blank} exam.  All of the information in this guide is a curation of study resources that the authors used to study for and pass the Cisco DCAUTO exam.

!!! attention
    All content in this guide strictly complies with the [Cisco Certification and Confidentiality Agreement](https://www.cisco.com/c/dam/en_us/training-events/downloads/certificationNDA.pdf "Cisco Certification and Confidentiality Agreement"){target=_blank}, also known as the Cisco Certification Non-Disclosure Agreement (**NDA**).  We welcome and appreciate any Cisco NDA-compliant contributions from the community.

!!! info
    - This guide is neither affiliated with Cisco Systems, Inc. nor any of its affiliates, including Cisco DevNet.
    - All materials in this guide are contributions from the community of Cisco DevNet enthusiasts and certification candidates.
    - Any references to pay-for-use study materials are free of sponsorship, affiliations, royalties, and payments of any kind.
        - We pay for these resources just like anyone else would, and we recommend the paid resources because we think they are highly valuable.

---

## Exam Topics

:notebook_with_decorative_cover: The [Cisco DCAUTO exam topics](https://learningnetwork.cisco.com/s/dcauto-exam-topics "Cisco DCAUTO Exam Topics"){target=_blank} cover a variety of skills.  Some of those skills are specific to Cisco products and solutions (ACI, Nexus, Intersight, etc.), while others are product-agnostic, foundational infrastructure automation and programmability skills (Git, Python, Ansible, etc.).

:books: This is the fourth DevNet exam that we've studied for, yet the first for which we struggled to find a curated set of resources from which to study.  As we amassed notes, links, and our own code snippets, we organized everything into categories corresponding to the four sections in the Exam Topics list, so there is no ambiguity about finding the resources you need.

---

## Getting Started

:rocket: For us, liftoff is the hardest part of the study process.  Getting our computers set up in a way that allows us to study and take notes _always_ seems to take _way_ more time than we think it will.  To make that process easier for you, we tried to make the study resources in this guide as portable and consumable as possible.

:computer: We think the best way to study for the DCAUTO exam is to have a great development environment, so we packaged one right into the [GitHub repository](https://github.com/wwt/dcauto-study-resources "DCAUTO Study Resources GitHub Repository"){target=_blank} which supports this site.  The study material content doesn't change whether you choose to use our development environment, use the files in the GitHub repository to build a development environment from source, or use your own development environment.  These are the tools that we *recommend* to get started with your DCAUTO exam study:

1. :fontawesome-solid-cloud: **An account registration with [Cisco DevNet](https://developer.cisco.com "Cisco DevNet"){target=_blank}**.

    !!! tip
        If possible, we recommend you register with and log on to Cisco DevNet with a [Cisco.com account](https://id.cisco.com/signin/register "Cisco.com Account Registration"){target=_blank} because the DevNet labs for [Cisco Intersight](https://www.intersight.com "Cisco Intersight"){target=_blank} require a Cisco.com account.

2. :fontawesome-brands-windows: :fontawesome-brands-apple: **A Windows or macOS computer with the following software installed**:
    - :fontawesome-brands-docker: [Docker Desktop](https://www.docker.com/products/docker-desktop "Docker Desktop Download"){target=_blank}.
    - :fontawesome-brands-git-alt: Git SCM from [Git-SCM](https://git-scm.com/downloads "Git-SCM Downloads"){target=_blank} or from a [Windows](https://community.chocolatey.org/packages/git "Git - Chocolatey for Windows"){target=_blank} or [macOS](https://brew.sh/ "Homebrew for macOS"){target=_blank} package manager.
    - :material-microsoft-visual-studio-code: [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code"){target=_blank}.
    - :material-security-network: Cisco [AnyConnect](https://developer.cisco.com/site/sandbox/anyconnect/ "Cisco AnyConnect VPN Client"){target=_blank} or [OpenConnect](http://www.infradead.org/openconnect/ "OpenConnect VPN Client"){target=_blank} VPN client.
    - :fontawesome-solid-server: A desktop hypervisor ([Parallels](https://www.parallels.com/products/desktop/ "Parallels for Mac"){target=_blank}, [VirtualBox](https://www.virtualbox.org "VirtualBox"){target=_blank}, [VMware Fusion](https://www.vmware.com/products/fusion.html "VMware Fusion"){target=_blank}, or [VMware Workstation Player](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html "VMware Workstation Player"){target=_blank}).

    !!! tip
        A desktop hypervisor is optional.  We found value/ease in using a desktop hypervisor to run local instances of the [Cisco UCS Platform Emulator](https://community.cisco.com/t5/unified-computing-system/ucs-platform-emulator-downloads-ucspe-4-1-2cpe1-ucspe-4-0-4epe1/ta-p/3648177 "Cisco UCS Platform Emulator"){target=_blank} although DevNet provides labs with sufficient access to UCS platforms.

3. :fontawesome-solid-terminal: **Your favorite terminal/shell program (iTerm, PowerShell, Bash, etc.).**

    !!! tip
        In our examples, we use a combination of the [Visual Studio Code Integrated Terminal](https://code.visualstudio.com/docs/editor/integrated-terminal "Visual Studio Code Integrated Terminal"){target=_blank}, [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7.1 "PowerShell Installation Instructions"){target=_blank} and the [macOS Terminal application](https://support.apple.com/guide/terminal/welcome/mac "macOS Terminal Application"){target=_blank}.

---

## Topic Navigation

???+ abstract "Development Environment Setup"
    - [Visual Studio Code Dev Container](sections/section_0.md "Visual Studio Code Dev Container")

??? abstract "Section 1.0 - Network Programmability Foundation"
    - [Section 1.0 - Network Programmability Foundation](sections/section_1.md "Network Programmability Foundation")

??? abstract "Section 2.0 - Controller Based Data Center Networking"
    - [Section 2.0 - Controller Based Data Center Networking](sections/section_2.md "Controller Based Data Center Networking")

??? abstract "Section 3.0 - Data Center Device-Centric Networking"
    - [Section 3.0 - Data Center Device-Centric Networking](sections/section_3.md "Data Center Device-Centric Networking")

??? abstract "Section 4.0 - Data Center Compute"
    - [Section 4.0 - Data Center Compute](sections/section_4.md "Data Center Compute")

??? abstract "Appendix"
    - [Appendix A - Lessons Learned](sections/appendix_a.md "Appendix A - Lessons Learned")
    - [Appendix B - Jupyter Lab Overview](sections/appendix_b.md "Appendix B - Jupyter Lab Overview")

---

## Let's Do This

:medal: You're already to get started! Click [this link](sections/section_0.md "Development Environment Setup") to setup your development environment.

--8<-- "includes/glossary.txt"
