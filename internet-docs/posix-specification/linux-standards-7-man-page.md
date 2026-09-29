# standards(7) — Linux Manual Page (C and UNIX Standards)

> **Source:** https://www.man7.org/linux/man-pages/man7/standards.7.html
> **Fetched:** 2026-09-25
> **Author / Publisher:** Linux man-pages project (Michael Kerrisk)
> **Type:** reference (man page)
> **Tags:** POSIX, SUS, ISO C, standards, POSIX.1-2024, POSIX.1-2017, ISO/IEC 9945

## Summary

The `standards(7)` Linux manual page briefly describes every C and UNIX standard referenced in the STANDARDS section of man pages. It is an excellent, compact chronological cross-reference for the entire POSIX / Single UNIX Specification / ISO C lineage, with the online location of each document.

## Key Concepts

- Covers Research Unix (V7), BSD, System V/SVID, the ISO C standards (K&R, C89–C23), and the POSIX + SUS family.
- Maps informal names (SUSv1–SUSv5, UNIX 95/98/03) to formal designations (IEEE 1003.1 editions, ISO/IEC 9945).
- POSIX/SUS man pages are provided in sections 0p (headers), 1p (commands), 3p (functions), e.g. `man 3p open`.

## Details

### POSIX and SUS timeline (from the page)
- **POSIX.1-1988** — first POSIX standard (IEEE Std 1003.1-1988). Name coined by Richard Stallman.
- **POSIX.1-1990** — Part 1 (IEEE 1003.1-1990 = ISO/IEC 9945-1:1990).
- **POSIX.2** — commands and utilities (IEEE 1003.2-1992 = ISO/IEC 9945-2:1993).
- **POSIX.1b** (formerly POSIX.4) — realtime facilities (IEEE 1003.1b-1993).
- **POSIX.1c** (formerly POSIX.4a) — threads (IEEE 1003.1c-1995).
- **POSIX.1d** — additional realtime (IEEE 1003.1d-1999).
- **POSIX.1g** — networking/sockets (IEEE 1003.1g-2000).
- **POSIX.1j** — advanced realtime (IEEE 1003.1j-2000).
- **POSIX.1-1996** — revision incorporating .1b and .1c (ISO/IEC 9945-1:1996).
- **XPG3 / XPG4 / XPG4v2 (Spec 1170)** — X/Open Portability Guides.
- **SUS (SUSv1)** — UNIX 95; **SUSv2** — UNIX 98 (Issue 5, 1997).
- **POSIX.1-2001 / SUSv3** — consolidation of POSIX.1, POSIX.2, SUS under the Austin Group; four parts XBD/XSH/XCU/XRAT; two conformance levels (POSIX and XSI = UNIX 03); aligned with C99.
- **POSIX.1-2008 / SUSv4** — 2008 revision; many optional interfaces became mandatory; SUSv4 adds X/Open Curses Issue 7. 2013 and 2016 editions add technical corrigenda.
- **POSIX.1-2017** — technically identical to POSIX.1-2008 2016 edition (IEEE 1003.1-2017); online at `9699919799`.
- **POSIX.1-2024 / SUSv5** — ratified 2024 (IEEE 1003.1-2024); aligned with **C17**; online at `9799919799`.
- **Other:** LFS (Large File Summit, 1996) for 64-bit file offsets on 32-bit systems.

## References

- POSIX.1-2024 HTML: https://pubs.opengroup.org/onlinepubs/9799919799/
- POSIX.1-2017 HTML: https://pubs.opengroup.org/onlinepubs/9699919799/
- Austin Group: http://www.opengroup.org/austin/
- Related pages: feature_test_macros(7), posixoptions(7), libc(7)

---
_Captured from https://www.man7.org/linux/man-pages/man7/standards.7.html on 2026-09-25. Content belongs to its original author(s)._
