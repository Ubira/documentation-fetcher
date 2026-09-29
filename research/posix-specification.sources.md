# POSIX Specification and Related Standards

- **Focus**: The POSIX standard (IEEE Std 1003.1 / ISO/IEC 9945 / The Open Group Base Specifications, Issue 8) and its related standards — the Single UNIX Specification, realtime/threads amendments, and the POSIX.13 realtime Application Environment Profiles, with extra coverage of the PSE51 Minimal Realtime System Profile
- **Created**: 2026-09-25
- **Last updated**: 2026-09-25
- **Status**: reviewed

## Sources

### POSIX base standard & Single UNIX Specification

1. **The Open Group Base Specifications Issue 8 (POSIX.1-2024 / IEEE Std 1003.1-2024)** — spec (web page, HTML edition)
   https://pubs.opengroup.org/onlinepubs/9799919799/
   Why: The authoritative, freely readable HTML edition of the current POSIX standard — the four volumes (XBD Base Definitions, XSH System Interfaces, XCU Shell & Utilities, XRAT Rationale).
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/opengroup-base-specifications-issue-8.md

2. **The Open Group Base Specifications Issue 7, 2018 edition (POSIX.1-2017 / IEEE Std 1003.1-2017)** — spec (web page, HTML edition)
   https://pubs.opengroup.org/onlinepubs/9699919799/
   Why: The widely deployed previous POSIX edition still referenced by most implementations and man pages; same four-volume structure as Issue 8.
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/opengroup-base-specifications-issue-7.md

3. **IEEE 1003.1-2024 — IEEE SA standard record** — spec (web page, standard metadata)
   https://standards.ieee.org/ieee/1003.1/7700/
   Why: Official IEEE Standards Association record for the current POSIX standard — status, publication date, superseded editions, and the in-progress Corrigendum 1 aligning it with ISO/IEC/IEEE 9945.
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/ieee-1003-1-2024-standard-record.md

4. **The Single UNIX Specification, Version 5 (2024) — Introduction** — spec/overview (web page)
   https://www.unix.org/overview.html
   Why: Explains how the SUS relates to POSIX.1-2024, the XSI option, portability/margin codes, option groups, and realtime/threads functional areas — the best conceptual map of the standard.
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/single-unix-specification-v5-overview.md

5. **The Austin Common Standards Revision Group** — docs (web page, maintainer hub)
   https://www.opengroup.org/austin/
   Why: Home of the joint IEEE / Open Group / ISO-IEC working group that maintains POSIX; tracks draft/publication status (e.g. ISO/IEC/IEEE 9945:2026) and defect reporting.
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/austin-common-standards-revision-group.md

6. **POSIX.1 Frequently Asked Questions (FAQ)** — docs (web page, FAQ)
   https://www.opengroup.org/austin/papers/posix_faq.html
   Why: Maintainer-authored FAQ covering what POSIX is, PASC/Austin Group, version history, the realtime amendments (1003.1b/c/d/j/q), the 1003.13 profiles, and certification.
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/posix-1-faq.md

7. **standards(7) — Linux manual page (C and UNIX Standards)** — reference (web page, man page)
   https://www.man7.org/linux/man-pages/man7/standards.7.html
   Why: Concise chronological reference for every POSIX/SUS/C standard (POSIX.1-1988 through POSIX.1-2024/SUSv5) with the online location of each — an excellent cross-reference index.
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/linux-standards-7-man-page.md

8. **POSIX — Wikipedia** — reference (web page, encyclopedia)
   https://en.wikipedia.org/wiki/POSIX
   Why: Broad overview of the POSIX family: naming history, the pre-1997 parts (POSIX.1, .1b realtime, .1c threads, .2), the 2001–2024 revisions, and OS conformance status (including PSE51/PSE52 RTOS support).
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/posix-wikipedia.md

### PSE51 & POSIX.13 realtime Application Environment Profiles (extra focus)

9. **Zephyr — POSIX Application Environment Profiles (AEP): PSE51 / PSE52 / PSE53** — docs (web page)
   https://docs.zephyrproject.org/latest/services/portability/posix/aep/index.html
   Why: The clearest modern, concrete definition of the PSE51 Minimal Realtime System Profile — the exact option groups and `_POSIX_*` feature macros it requires, expressed against current POSIX-1.
   Verified: 2026-09-25
   Archived: internet-docs/posix-specification/pse51/zephyr-posix-application-environment-profiles.md

10. **Zephyr — POSIX Support Overview (Subprofiles)** — docs (web page)
    https://docs.zephyrproject.org/latest/services/portability/posix/overview/index.html
    Why: Frames why RTOSes use POSIX subprofiles (PSE51–PSE54) instead of full conformance, links PSE51 to the IEEE 1003.1-2017 subprofiling options, and shows a minimal PSE51-style app.
    Verified: 2026-09-25
    Archived: internet-docs/posix-specification/pse51/zephyr-posix-support-overview.md

11. **POSIX 1003.13 Profiles — Overview (The Open Group)** — docs (web page)
    https://www.opengroup.org/testing/testsuites/POSIXProfiles.htm
    Why: Original Open Group description of Profiles 51–54, including the single/multi-process vs. file-system matrix that distinguishes PSE51 from PSE52/53/54, plus the VSPSE test suites.
    Verified: 2026-09-25
    Archived: internet-docs/posix-specification/pse51/opengroup-posix-1003-13-profiles.md

12. **IEEE 1003.13-2003 — IEEE SA standard record** — spec (web page, standard metadata)
    https://standards.ieee.org/ieee/1003.13/3322/
    Why: Official IEEE record for the Standardized Application Environment Profile (POSIX Realtime & Embedded Application Support) that formally defines PSE51–PSE54; documents its status (Inactive-Reserved) and history.
    Verified: 2026-09-25
    Archived: internet-docs/posix-specification/pse51/ieee-1003-13-2003-standard-record.md

13. **IEEE P1003.13 Draft (posix_13.book) — University of York RTS group** — spec (downloadable PDF)
    https://www.cs.york.ac.uk/rts/docs/P1003.13-posix_D2.1.pdf
    Why: A publicly hosted draft of the POSIX.13 realtime profile standard — the fullest freely available text defining the PSE51/52/53/54 profiles and their Units of Functionality.
    Verified: 2026-09-25
    Archived: internet-docs/posix-specification/pse51/ieee-p1003-13-draft-D2.1.pdf

---

13 links verified — official POSIX/Open Group specs (Issue 8, Issue 7, SUSv5, Austin Group, FAQ) + IEEE SA standard records (1003.1-2024, 1003.13-2003) + reference pages (man7 standards(7), Wikipedia) + PSE51-focused material (2 Zephyr docs, Open Group 1003.13 profiles, York draft PDF). All 13 archived under internet-docs/posix-specification/.
