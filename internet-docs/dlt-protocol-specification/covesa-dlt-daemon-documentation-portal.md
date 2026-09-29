# COVESA dlt-daemon — Documentation Portal

> **Source:** https://covesa.github.io/dlt-daemon/
> **Fetched:** 2026-09-24
> **Author / Publisher:** COVESA (Connected Vehicle Systems Alliance)
> **Type:** documentation portal
> **Tags:** dlt, diagnostic-log-and-trace, covesa, autosar, documentation, dlt-daemon

## Summary

The rendered GitHub Pages documentation site for the COVESA DLT reference implementation. It mirrors the repository README and links out to the full documentation set — glossary, developer guide, design specification, build options and advanced-feature guides. This is the best offline entry point for navigating DLT's conceptual and how-to documentation.

## Key Concepts

- COVESA DLT supports two protocol versions: **V1** (AUTOSAR Classic Platform R19-11 DLT) and **V2** (AUTOSAR Classic Platform R22-11 DLT, MVP).
- Roles: DLT User, DLT Library (`libdlt`), DLT Daemon, DLT Client (with injection messages).
- The site is organized as Overview → Get Started → Learn more → Contribution.

## Details

### Documentation links (rendered)

- **Overview & Get Started** — build/install, run a DLT demo (`doc/dlt_demo_setup.md`), develop your own DLT app (`doc/dlt_for_developers.html`).
- **Glossary** — `doc/dlt_glossary.html`.
- **Design specifications** — `doc/dlt_design_specification.md` (daemon/library internals).
- **DLT Daemon V2** — `doc/dlt_daemon_v2.md`.
- **Build options** — `doc/dlt_build_options.html`.
- **Advanced topics** — LogStorage, MultiNode, Extended Network Trace, DLT Filetransfer, DLT KPI, DLT Core Dump Handler.
- **Man pages** (generated with `-DWITH_MAN=ON`) — `dlt-daemon(1)`, `dlt.conf(5)`, `dlt-receive(1)`, `dlt-control(1)`, `dlt-logstorage-ctrl(1)`, `dlt-system(1)`, adaptors, `dlt-convert(1)`, etc.
- **Release notes** — `ReleaseNotes.html`.
- **Code coverage** — LCOV report at `dlt_lcov_report/index.html`.

### Get started (build)

```bash
sudo apt-get install cmake zlib1g-dev libdbus-glib-1-dev build-essential
git clone https://github.com/COVESA/dlt-daemon.git
cd dlt-daemon && mkdir build && cd build
cmake ..
make
# optional:
sudo make install
```

To build API docs (doxygen): `cmake -DWITH_DOC=ON .. && make doc`.
To build man pages: `cmake -DWITH_MAN=ON .. && make generate_man`.

## References

- Repository: https://github.com/COVESA/dlt-daemon
- Design spec: https://covesa.github.io/dlt-daemon/doc/dlt_design_specification.md
- Developer guide: https://covesa.github.io/dlt-daemon/doc/dlt_for_developers.html
- Glossary: https://covesa.github.io/dlt-daemon/doc/dlt_glossary.html
- COVESA project page: https://covesa.global/project/diagnostic-log-trace/

---
_Captured from https://covesa.github.io/dlt-daemon/ on 2026-09-24. Content belongs to its original author(s) (COVESA, MPL-2.0)._
