# COVESA dlt-daemon — Repository Overview (README)

> **Source:** https://github.com/COVESA/dlt-daemon
> **Fetched:** 2026-09-24
> **Author / Publisher:** COVESA (Connected Vehicle Systems Alliance)
> **Type:** repo overview
> **Tags:** dlt, diagnostic-log-and-trace, autosar, covesa, automotive, logging, dlt-daemon, libdlt

## Summary

The canonical open-source implementation of the automotive Diagnostic Log and Trace (DLT) protocol, maintained by COVESA. DLT provides a standardized logging and tracing interface for ECUs. The repository contains the DLT daemon, the DLT user library (`libdlt`), console utilities, adaptors and test applications. It supports two protocol versions: V1 (based on AUTOSAR Classic Platform R19-11) and V2 (based on AUTOSAR Classic Platform R22-11, released as an MVP).

## Key Concepts

- **Protocol versions**: V1 = AUTOSAR CP R19-11 DLT (stable, widely adopted); V2 = AUTOSAR CP R22-11 DLT (MVP, limited feature set). See `doc/dlt_daemon_v2.md`.
- **Core components**:
  - **DLT User** — an application producing DLT log messages via the library.
  - **DLT Library (`libdlt`)** — API to craft messages and hand them to the daemon; caches to a ring buffer if the daemon is unavailable.
  - **DLT Daemon** — the ECU's DLT communication interface; collects/buffers messages and serves DLT clients; accepts control messages.
  - **DLT Client** — receives/consumes log messages from daemons; can issue control and injection messages.
- **License**: MPL-2.0.
- **Latest release noted**: v3.0.0 "DLT Protocol v2".

## Details

### Build and install

Dependencies: `cmake`, `zlib`, `dbus`, optional `json-c` (for `dlt-receive` extended filtering).

```bash
sudo apt-get install cmake zlib1g-dev libdbus-glib-1-dev build-essential
# optional:
sudo apt-get install libjson-c-dev

git clone https://github.com/COVESA/dlt-daemon.git
cd dlt-daemon
mkdir build && cd build
cmake ..
make
# optional:
sudo make install
sudo ldconfig
```

CMake accepts many build options (see `doc/dlt_build_options.md`).

### Advanced topics

- **Build Options** — turn features on/off, choose alternative implementations.
- **LogStorage** — buffering/caching log data, writing to mass storage for long-term storage.
- **MultiNode** — a daemon acting as gateway connecting multiple passive nodes.
- **Extended Network Trace** — send/truncate messages that exceed normal DLT message size limits.
- **DLT Filetransfer** — transmit files over DLT (decoded by e.g. DLT Viewer).
- **DLT KPI** — read system status information (from `/proc`) via DLT.
- **DLT Core Dump Handler** — collect debug info and transfer via DLT Filetransfer.

### Configure, control and interface (man pages, `-DWITH_MAN=ON`)

- `dlt-daemon(1)`, `dlt.conf(5)` — start and configure the daemon.
- `dlt-receive(1)` / `dlt-receive-v2` — receive and print/store messages (V1/V2).
- `dlt-control(1)` / `dlt-control-v2` — send control messages (V1/V2).
- `dlt-logstorage-ctrl(1)` — trigger logstorage connect/disconnect/sync.
- `dlt-passive-node-ctrl(1)` — connect/disconnect a passive daemon.
- `dlt-system(1)` / `dlt-system.conf(5)` — access system logs via DLT.
- `dlt-adaptor-stdin(1)` / `dlt-adaptor-udp(1)` — forward stdin/UDP to daemon.
- `dlt-convert(1)` — convert DLT files to human-readable format.
- `dlt-sortbytimestamp(1)` — sort messages by timestamp.
- `dlt-qnx-system(1)` — access QNX system logs via DLT.

### Known issues

- `dlt_user_log_write_float64()` / `DLT_FLOAT64()` can crash on ARM targets.
- Nested `DLT_LOG_...` calls are unsupported and can deadlock.
- On non-Linux platforms (e.g. QNX) only UNIX_SOCKET IPC is supported; Linux supports both FIFO and UNIX_SOCKET.

## Code Examples

```c
#include <dlt/dlt.h>

DLT_DECLARE_CONTEXT(ctx)

int main(void)
{
    DLT_REGISTER_APP("TAPP", "Test Application for Logging");
    DLT_REGISTER_CONTEXT(ctx, "TES1", "Test Context for Logging");

    DLT_LOG(ctx, DLT_LOG_ERROR, DLT_CSTRING("This is an error"));

    DLT_UNREGISTER_CONTEXT(ctx);
    DLT_UNREGISTER_APP();
    return 0;
}
```

## References

- Design specification: https://github.com/COVESA/dlt-daemon/blob/master/doc/dlt_design_specification.md
- DLT for developers guide: https://github.com/COVESA/dlt-daemon/blob/master/doc/dlt_for_developers.md
- Glossary: https://github.com/COVESA/dlt-daemon/blob/master/doc/dlt_glossary.md
- Rendered docs: https://covesa.github.io/dlt-daemon/
- AUTOSAR CP R19-11 DLT (V1 basis): https://www.autosar.org/fileadmin/standards/R19-11/CP/AUTOSAR_SWS_DiagnosticLogAndTrace.pdf
- AUTOSAR CP R22-11 DLT (V2 basis): https://www.autosar.org/fileadmin/standards/R22-11/CP/AUTOSAR_SWS_DiagnosticLogAndTrace.pdf

---
_Captured from https://github.com/COVESA/dlt-daemon on 2026-09-24. Content belongs to its original author(s) (COVESA, MPL-2.0)._
