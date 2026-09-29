# POSIX 1003.13 Profiles — Overview (The Open Group)

> **Source:** https://www.opengroup.org/testing/testsuites/POSIXProfiles.htm
> **Fetched:** 2026-09-25
> **Author / Publisher:** The Open Group
> **Type:** docs
> **Tags:** PSE51, PSE52, PSE53, PSE54, POSIX.13, realtime profiles, Units of Functionality, VSPSE test suites

## Summary

The Open Group's overview of the **POSIX 1003.13 Profiles 51–54**, which provide four levels of functionality to which realtime environments can conform. The profiles are snapshots along a continuum of realtime capability, based on a study of existing commercial practice. This page also introduces the VSPSE conformance test suites.

## Key Concepts

- All profiles include some or all of **POSIX .1, .1b (realtime), and .1c (threads)**, plus parts of POSIX .2 / .2a for the development platform (typically a host for Profiles 51–53).
- The four profiles differ by **process model** (single vs. multi) and **file-system** presence:

| | Single process | Multi process |
| --- | --- | --- |
| **No file system** | **PSE51** | **PSE53** |
| **File system** | **PSE52** | **PSE54** |

- **PSE51** = Minimal Realtime System: single process, no file system.
- **PSE52** = Realtime Controller: single process, with file system.
- **PSE53** = Dedicated Realtime System: multi process, no file system.
- **PSE54** = Multi-Purpose Realtime System: multi process, with file system.

## Details

### Conformance test suites
- **VSPSE52** — for Profile 52; a merged subset of VSX4, VSTH (Threads), and VSRT (Realtime).
- **VSPSE54** — modifies VSX4, VSTH, and VSRT so coverage can be limited to the Units of Functionality of a Profile 54 environment.

(Page last updated 11 September 2003; © The Open Group 1995–2010.)

## References

- VSPSE52: https://www.opengroup.org/testing/testsuites/VSPSE52.htm
- VSPSE54: https://www.opengroup.org/testing/testsuites/VSPSE54.htm
- IEEE 1003.13-2003 record: https://standards.ieee.org/ieee/1003.13/3322/

---
_Captured from https://www.opengroup.org/testing/testsuites/POSIXProfiles.htm on 2026-09-25. Content belongs to its original author(s)._
