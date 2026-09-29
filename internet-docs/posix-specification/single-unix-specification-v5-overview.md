# The Single UNIX Specification, Version 5 (2024) — Introduction

> **Source:** https://www.unix.org/overview.html
> **Fetched:** 2026-09-25
> **Author / Publisher:** The Open Group
> **Type:** spec / overview
> **Tags:** Single UNIX Specification, SUSv5, POSIX.1-2024, XSI, X/Open Curses, portability codes, realtime, threads

## Summary

An introduction to the **Single UNIX Specification, Version 5 (2024)** — the superset specification that a system must satisfy to use the UNIX trademark. Its core documents are **The Open Group Base Specifications, Issue 8**, which are also **POSIX.1-2024**. This page is the best conceptual map of how POSIX, the XSI option, X/Open Curses, portability/margin codes, and realtime/threads option groups fit together.

## Key Concepts

- SUSv5 = **Base Specifications, Issue 8** (XBD, XSH, XCU, XRAT) **plus X/Open Curses, Issue 8**.
- Standards alignment: technically identical to POSIX.1-2024, and aligned with **ISO/IEC 9899 (ISO C)**. As of this version the C binding is **C17** (utility `c17`).
- **XSI (X/Open System Interfaces)** marks functionality mandatory on UNIX-certified systems but optional in base POSIX.
- Feature test macro: define `_XOPEN_SOURCE` to **800** (equivalent to `_POSIX_C_SOURCE` = **202405L**) to expose SUSv5 functionality.
- Focus is application development / portability, not system management.

## Details

### Portability (margin) codes
There are **45 margin codes** defined in XBD §2.1.6. 40 reflect optional POSIX-base features (six of which are mandatory in SUS: **FSC, TSA, TSH, TSS, UP, XSI**). Notable realtime/threads codes:
- **ADV** Advisory Information (Advanced Realtime)
- **CPT** Process CPU-Time Clocks (Advanced Realtime)
- **ML / MLR** Process / Range Memory Locking (Realtime)
- **MSG** Message Passing (Realtime)
- **PIO** Prioritized Input and Output
- **PS** Process Scheduling (Realtime)
- **SHM** Shared Memory Objects (Realtime)
- **SIO** Synchronized Input and Output (Realtime)
- **SPN** Spawn (Advanced Realtime)
- **SS / TSP** Process / Thread Sporadic Server (Advanced Realtime [Threads])
- **TCT** Thread CPU-Time Clocks (Advanced Realtime Threads)
- **TPS** Thread Execution Scheduling (Realtime Threads)
- **TPI / TPP / RPI / RPP** Mutex Priority Inheritance/Protection variants
- **TYM** Typed Memory Objects (Advanced Realtime)
- **OB** Obsolescent, **OH** Optional Header, **OF** Output Format Incompletely Specified.

### Option Groups (functional areas)
- **Realtime** — functions from IEEE Std 1003.1b-1993.
- **Realtime Threads** — threads-related realtime functions.
- **Advanced Realtime** — non-threads functions from IEEE Std 1003.1d-1999 and 1003.1j-2000.
- **Advanced Realtime Threads** — threads functions from 1003.1d-1999 and 1003.1j-2000.
- **Tracing** — from IEEE Std 1003.1q-2000 (marked obsolescent in this version).
- **Encryption** — `crypt()`, `encrypt()`, `setkey()`.

### Programming environment topics
- C-language support (ISO C / c17), feature test macros and name space, error numbers (`errno`), reliable signal concepts, standard I/O streams, **Realtime** (semaphores, memory locking, mapped files/shared memory, priority scheduling, realtime signals, timers, IPC, sync/async I/O), **Threads** (mutexes, attributes, scheduling, cancelation, read-write locks, app-managed stacks), **Sockets** (UNIX-domain, IPv4/IPv6, raw), and the General Terminal Interface.

### Commands & utilities
- Standardizes **174 utilities**; the shell is the standard POSIX shell (Bourne-based with KornShell features).
- Also covers symbolic links, file format notation, BRE/ERE regular expressions, YACC grammars as specifications, and internationalization (I18N/locales, multibyte/wide-character handling, message catalogs, codeset conversion).

## References

- XBD Contents: https://www.unix.org/xbd_contents.html
- UNIX certification: https://www.opengroup.org/certifications/unix
- POSIX.1-2024 HTML edition: https://pubs.opengroup.org/onlinepubs/9799919799/

---
_Captured from https://www.unix.org/overview.html on 2026-09-25. Content belongs to its original author(s)._
