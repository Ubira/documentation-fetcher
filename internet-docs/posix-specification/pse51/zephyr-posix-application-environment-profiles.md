# Zephyr — POSIX Application Environment Profiles (AEP): PSE51 / PSE52 / PSE53

> **Source:** https://docs.zephyrproject.org/latest/services/portability/posix/aep/index.html
> **Fetched:** 2026-09-25
> **Author / Publisher:** Zephyr Project
> **Type:** docs
> **Tags:** PSE51, PSE52, PSE53, POSIX.13, AEP, realtime, IEEE 1003.13-2003, IEEE 1003.1-2017, RTOS

## Summary

Zephyr's reference page defining the POSIX **Application Environment Profiles (AEP)**. Although **IEEE 1003.13-2003** is inactive, it defined the AEPs that inspired the subprofiling options of **IEEE 1003.1-2017**. This page restates the single-purpose realtime profiles — **PSE51 (Minimal Realtime System)**, **PSE52 (Realtime Controller)**, and **PSE53 (Dedicated Realtime System)** — in terms that agree with the current POSIX-1 standard, listing the exact option groups and `_POSIX_*` feature-macro values each requires. This is the clearest modern, concrete definition of what PSE51 actually contains.

## Key Concepts

- Profiles are cumulative: PSE52 includes PSE51; PSE53 includes PSE52 + PSE51; all include the required POSIX **System Interfaces**. **PSE54** is not considered by Zephyr.
- PSE51 is the **minimal realtime** profile: single process, no file system required — targeted at small MCU/embedded systems.

## Details

### Minimal Realtime System Profile (PSE51)
Marker: `_POSIX_AEP_REALTIME_MINIMAL` (Kconfig `CONFIG_POSIX_AEP_REALTIME_MINIMAL`).

Required option groups:
| Option Group | Status | Kconfig |
| --- | --- | --- |
| POSIX_C_LANG_JUMP | yes | |
| POSIX_C_LANG_SUPPORT | yes | |
| POSIX_DEVICE_IO | yes | CONFIG_POSIX_DEVICE_IO |
| POSIX_SIGNALS | yes | CONFIG_POSIX_SIGNALS |
| POSIX_SINGLE_PROCESS | yes | CONFIG_POSIX_SINGLE_PROCESS |
| XSI_THREADS_EXT | yes | CONFIG_XSI_THREADS_EXT |

Required options (`_POSIX_*` = 200809L unless noted):
`_POSIX_FSYNC`, `_POSIX_MEMLOCK`, `_POSIX_MEMLOCK_RANGE`, `_POSIX_MONOTONIC_CLOCK`, `_POSIX_SHARED_MEMORY_OBJECTS`, `_POSIX_SYNCHRONIZED_IO`, `_POSIX_THREAD_ATTR_STACKADDR`, `_POSIX_THREAD_ATTR_STACKSIZE`, `_POSIX_THREAD_CPUTIME`, `_POSIX_THREAD_PRIO_INHERIT`, `_POSIX_THREAD_PRIO_PROTECT`, `_POSIX_THREAD_PRIORITY_SCHEDULING`. (`_POSIX_THREAD_SPORADIC_SERVER` = -1, i.e. not required.)

### Realtime Controller System Profile (PSE52)
Adds (on top of PSE51): `POSIX_C_LANG_MATH`, `POSIX_FD_MGMT`, `POSIX_FILE_SYSTEM`, and `_POSIX_MESSAGE_PASSING` (200809L). Trace options `_POSIX_TRACE*` are not required (-1).

### Dedicated Realtime System Profile (PSE53)
Adds (on top of PSE52/PSE51): `POSIX_MULTI_PROCESS`, `POSIX_NETWORKING`, `POSIX_PIPE`, `POSIX_SIGNAL_JUMP`, plus options such as `_POSIX_CPUTIME`, `_POSIX_RAW_SOCKETS` (200809L). Some (e.g. `_POSIX_PRIORITIZED_IO`, `_POSIX_PRIORITY_SCHEDULING`, `_POSIX_SPAWN`, `_POSIX_SPORADIC_SERVER`) are not required.

## References

- IEEE 1003.13-2003 record: https://standards.ieee.org/ieee/1003.13/3322/
- IEEE 1003.1-2017 record: https://standards.ieee.org/ieee/1003.1/7101/
- Required System Interfaces: https://docs.zephyrproject.org/latest/services/portability/posix/conformance/index.html#posix-system-interfaces-required
- Zephyr POSIX overview: https://docs.zephyrproject.org/latest/services/portability/posix/overview/index.html

---
_Captured from https://docs.zephyrproject.org/latest/services/portability/posix/aep/index.html on 2026-09-25. Content belongs to its original author(s)._
