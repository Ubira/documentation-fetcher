# POSIX — Wikipedia

> **Source:** https://en.wikipedia.org/wiki/POSIX
> **Fetched:** 2026-09-25
> **Author / Publisher:** Wikipedia contributors (CC BY-SA 4.0)
> **Type:** reference (encyclopedia article)
> **Tags:** POSIX, IEEE 1003, ISO/IEC 9945, Single UNIX Specification, pthreads, realtime, PSE51, conformance

## Summary

Wikipedia's overview of **POSIX (Portable Operating System Interface, IEEE 1003)** — a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems, covering API, shell, and utilities. Developed by the **Austin Group** (IEEE, The Open Group, ISO/IEC JTC 1/SC 22/WG 15); the ISO/IEC number is **ISO/IEC 9945**. Useful for naming history, the pre-1997 parts, the modern revisions, and a large OS-conformance list.

## Key Concepts

- Name suggested by Richard Stallman; originally referred to IEEE Std 1003.1-1988.
- Latest version: **IEEE Std 1003.1-2024** (published 14 June 2024), aligned with the **C17** language standard.
- After 1997 the Austin Group publishes the Single UNIX Specification (SUS); POSIX is then amended per a SUS version. SUS volumes carry an "issue" number distinct from the version (e.g. SUSv3 = issue 6).

## Details

### Pre-1997 parts
- **POSIX.1** (IEEE 1003.1-1988) — Core Services: process creation/control, signals, file/directory ops, pipes, C library, POSIX terminal interface.
- **POSIX.1b** (IEEE 1003.1b-1993, later `librt`) — Real-time extensions: priority scheduling, real-time signals, clocks/timers, semaphores, message passing, shared memory, async/sync I/O, memory locking.
- **POSIX.1c** (IEEE 1003.1c-1995) — Threads: creation/control/cleanup, scheduling, synchronization, signal handling.
- **POSIX.2** (IEEE 1003.2-1992) — Shell and Utilities.

### Modern revisions
- **POSIX.1-2001** (mostly SUSv3, issue 6); IEEE 1003.1-2004 adds two corrigenda.
- **POSIX.1-2008** (IEEE 1003.1-2008, 2016 Edition; SUSv4).
- **POSIX.1-2017** — two technical corrigenda over 2008.
- **POSIX.1-2024** — current; C17-aligned.

### Conformance highlights
- **Certified** (current): AIX, INTEGRITY, macOS (Leopard → Tahoe), OpenServer, UnixWare, VxWorks, z/OS.
- **Partially conformant**: FreeBSD, Linux (most distros), NetBSD, OpenBSD, illumos, Minix 3, NuttX, Redox, SerenityOS, Zephyr, etc.
- **RTOS profile note:** PikeOS is an RTOS with optional **PSE51 and PSE52** partitions; **RTEMS** provides POSIX API support designed to **IEEE Std 1003.13-2003 PSE52**.
- **Compatibility layers / subsystems**: Cygwin, MinGW, WSL, Microsoft POSIX subsystem/Interix/SUA, UWIN, MKS Toolkit, etc.

## References

- Base Specifications Issue 8: https://pubs.opengroup.org/onlinepubs/9799919799/
- POSIX Certification home: https://posix.opengroup.org/
- Austin Group: https://www.opengroup.org/austin/
- POSIX.1 FAQ: https://www.opengroup.org/austin/papers/posix_faq.html

---
_Captured from https://en.wikipedia.org/wiki/POSIX on 2026-09-25. Text available under CC BY-SA 4.0; content belongs to its original author(s)._
