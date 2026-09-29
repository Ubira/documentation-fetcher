# Zephyr — POSIX Support Overview (Subprofiles)

> **Source:** https://docs.zephyrproject.org/latest/services/portability/posix/overview/index.html
> **Fetched:** 2026-09-25
> **Author / Publisher:** Zephyr Project
> **Type:** docs / overview
> **Tags:** PSE51, PSE52, PSE53, PSE54, POSIX subprofiles, POSIX.13-2003, IEEE 1003.1-2017, RTOS, embedded

## Summary

Zephyr's POSIX overview explains why real-time operating systems adopt **POSIX subprofiles** (PSE51–PSE54) rather than full POSIX conformance, and how those profiles — originally from **IEEE 1003.13-2003 (POSIX.13-2003)** — are now captured as **Options and Option Groups** in **IEEE 1003.1-2017**. It provides the practical, RTOS-oriented context for the PSE51 Minimal Realtime System Profile.

## Key Concepts

- Zephyr implements a subset of POSIX defined by **IEEE 1003.1-2017 (POSIX-1.2017)**.
- Because an RTOS typically runs as a single process in a shared address space with limited resources, full POSIX conformance is impractical — hence subprofiles.
- The four Application Environment Profiles, each adding features over the required POSIX System Interfaces:
  - **PSE51** — Minimal Realtime System Profile
  - **PSE52** — Realtime Controller System Profile
  - **PSE53** — Dedicated Realtime System Profile
  - **PSE54** — Multi-Purpose Realtime System
- POSIX.13-2003 AEPs were formalized via "Units of Functionality" but the spec is now **inactive** (reference only); the intent lives on in POSIX-1.2017 §E Subprofiling Considerations.

## Details

### Configuring a subprofile in Zephyr (Kconfig)
- `CONFIG_POSIX_AEP_CHOICE_BASE`
- `CONFIG_POSIX_AEP_CHOICE_PSE51`
- `CONFIG_POSIX_AEP_CHOICE_PSE52`
- `CONFIG_POSIX_AEP_CHOICE_PSE53`

Additional options (e.g. `CONFIG_POSIX_C_LIB_EXT=y`) can be enabled as needed. The legacy `CONFIG_POSIX_API` is now frozen and roughly equivalent to PSE51 plus `CONFIG_POSIX_FD_MGMT`, `CONFIG_POSIX_MESSAGE_PASSING`, and `CONFIG_POSIX_NETWORKING`; it should not be used for new applications.

### Minimal PSE51-style example
```c
#include <stddef.h>
#include <stdio.h>
#include <time.h>

void megasleep(size_t megaseconds)
{
    struct timespec ts = {
        .tv_sec = megaseconds * 1000000,
        .tv_nsec = 0,
    };

    printf("See you in a while!\n");
    if (nanosleep(&ts, NULL) == -1) {
        perror("nanosleep");
    }
}

int main()
{
    megasleep(42);
    return 0;
}
```
```conf
# prj.conf
CONFIG_POSIX_API=y
```

### Why POSIX on an RTOS
- Familiar API for non-embedded (Linux) programmers.
- Reuse/portability of existing POSIX-based libraries.
- An efficient API subset suitable for small MCU systems (cf. Zephyr, AWS:FreeRTOS, TI-RTOS, NuttX).

## References

- IEEE 1003.1-2017, Section E, Subprofiling Considerations: https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html
- IEEE 1003.13-2003 record: https://standards.ieee.org/ieee/1003.13/3322/
- Zephyr AEP (PSE51/52/53) details: https://docs.zephyrproject.org/latest/services/portability/posix/aep/index.html

---
_Captured from https://docs.zephyrproject.org/latest/services/portability/posix/overview/index.html on 2026-09-25. Content belongs to its original author(s)._
