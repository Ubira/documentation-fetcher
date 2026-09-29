# AUTOSAR Adaptive Platform — Standards Landing Page

> **Source:** https://www.autosar.org/standards/adaptive-platform
> **Fetched:** 2026-09-24
> **Author / Publisher:** AUTOSAR
> **Type:** docs (overview / hub page)
> **Tags:** AUTOSAR, Adaptive Platform, ARA, functional clusters, software architecture, AP_EXP_SWArchitecture

## Summary

This is the official AUTOSAR landing page for the Adaptive Platform. It explains the
purpose of the Adaptive Platform, introduces the AUTOSAR Runtime for Adaptive
Applications (ARA), describes the concept of functional clusters and the Adaptive
Platform Basis, and links out to every document released for the current standard
(R25-11 at time of capture), including the *Explanation of Adaptive Platform Software
Architecture* (`AUTOSAR_AP_EXP_SWArchitecture`). It is the canonical entry point for
navigating the Adaptive Platform architecture, methodology, templates, and tools.

## Key Concepts

- **ARA (AUTOSAR Runtime for Adaptive Applications):** The runtime implemented by the
  Adaptive Platform. It exposes two kinds of interfaces — **services** and **APIs**.
- **Functional clusters:** The building blocks of the platform. They:
  - assemble functionalities of the Adaptive Platform,
  - define the clustering of the requirements specification,
  - describe the behavior of the software platform from the application and network
    perspective,
  - but do **not** constrain the final SW design of the architecture implementing the
    Adaptive Platform.
- **Adaptive Platform Basis:** Functional clusters in the Basis must have at least one
  instance per (virtual) machine, whereas services may be distributed across the in-car
  network.
- **Dynamic linking:** In contrast to the Classic Platform, the Adaptive Platform runtime
  environment dynamically links services and clients during runtime.
- **Current release:** AUTOSAR Adaptive Release **R25-11** (with past releases archived).

## Details

### Architecture areas covered by the Adaptive Platform documentation set

The landing page organizes the Adaptive Platform into architectural elements, each of
which links to its released specification documents:

- Introduction
- Adaptive Application (1..n)
- Runtime
- Communication
- Storage
- Security
- Safety
- Configuration
- Diagnostics
- Cryptography
- POSIX OS (references the Open Group POSIX.1-2017 / 2018 edition)
- (Virtual) Machine

### Additional document categories

The Adaptive Platform also provides:

- **Common Documents & Libraries**
- **Methodology** — AUTOSAR extends the existing Methodology to provide a common approach
  across Classic and Adaptive Platforms, supporting distributed, independent, and agile
  development. It standardizes work products (services, applications, machines, and their
  configuration) and the tasks that exchange design information between them.
- **Tools**
- **Templates**

### Where `AUTOSAR_AP_EXP_SWArchitecture` fits

The *Explanation of Adaptive Platform Software Architecture* is an **EXP** (explanatory)
document under the Adaptive Platform. It gives the architectural overview that ties the
functional clusters listed above into a coherent software architecture, and is
complemented by `AUTOSAR_AP_EXP_PlatformDesign` (Explanation of Adaptive Platform Design).

### Important notice (from AUTOSAR)

All files are made available for download for the purpose of INFORMATION ONLY. The
material is protected by copyright and other intellectual property rights; commercial
exploitation requires an AUTOSAR partnership/license. See the disclaimer inside each file
and the AUTOSAR Terms of Use.

## References

- AUTOSAR Adaptive Platform (this page): https://www.autosar.org/standards/adaptive-platform
- Current release filter (R25-11 AP documents): https://www.autosar.org/search?tx_solr%5Bfilter%5D%5B1%5D=platform%3AAP&tx_solr%5Bfilter%5D%5B2%5D=category%3AR25-11&tx_solr%5Bq%5D=
- AUTOSAR Standards overview: https://www.autosar.org/standards
- AUTOSAR Terms of Use: https://www.autosar.org/fileadmin/user_upload/Documents/AUTOSAR_Terms_Of_Use.pdf
- POSIX.1-2017 (referenced OS baseline): https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/

---
_Captured from https://www.autosar.org/standards/adaptive-platform on 2026-09-24. Content belongs to its original author(s) (AUTOSAR)._
