# DLT (Diagnostic Log and Trace) Protocol Specification

- **Focus**: Message/wire format and protocol specification of the automotive Diagnostic Log and Trace (DLT) protocol — AUTOSAR Classic Platform (DLT) and Adaptive Platform (Log and Trace / `ara::log`), plus the COVESA reference implementation
- **Created**: 2026-09-24
- **Last updated**: 2026-09-28
- **Status**: reviewed

## Sources

### Classic Platform & COVESA implementation

1. **AUTOSAR FO PRS Log and Trace Protocol Specification (Foundation R25-11, latest)** — spec (downloadable PDF)
   https://www.autosar.org/fileadmin/standards/R25-11/FO/AUTOSAR_FO_PRS_LogAndTraceProtocol.pdf
   Why: Latest AUTOSAR Foundation release of the DLT wire-format protocol spec — base/extended header, verbose vs. non-verbose mode, message sequences and semantics.
   Verified: 2026-09-28
   Archived: internet-docs/autosar-log-and-trace/protocol/AUTOSAR_FO_PRS_LogAndTraceProtocol_R25-11.pdf

2. **AUTOSAR PRS Log and Trace Protocol Specification (R23-11)** — spec (downloadable PDF)
   https://www.autosar.org/fileadmin/standards/R23-11/FO/AUTOSAR_FO_PRS_LogAndTraceProtocol.pdf
   Why: R23-11 Foundation release of the Log and Trace protocol spec — retained for comparison against the latest R25-11 protocol format.
   Verified: 2026-09-24
   Archived: internet-docs/autosar-log-and-trace/protocol/AUTOSAR_FO_PRS_LogAndTraceProtocol_R23-11.pdf

3. **AUTOSAR PRS Log and Trace Protocol Specification (R22-11)** — spec (downloadable PDF)
   https://www.autosar.org/fileadmin/standards/R22-11/FO/AUTOSAR_PRS_LogAndTraceProtocol.pdf
   Why: R22-11 Protocol Requirements Specification defining the DLT wire format — retained as the baseline matching the COVESA V2 implementation.
   Verified: 2026-09-24
   Archived: internet-docs/autosar-log-and-trace/protocol/AUTOSAR_PRS_LogAndTraceProtocol.pdf

4. **AUTOSAR CP SWS Diagnostic Log and Trace (Classic Platform R25-11, latest)** — spec (downloadable PDF)
   https://www.autosar.org/fileadmin/standards/R25-11/CP/AUTOSAR_CP_SWS_DiagnosticLogAndTrace.pdf
   Why: Latest Classic Platform Software Specification for the DLT module — module behaviour, configuration parameters and the Dlt header.
   Verified: 2026-09-28
   Archived: internet-docs/autosar-log-and-trace/classic-platform/AUTOSAR_CP_SWS_DiagnosticLogAndTrace_R25-11.pdf

5. **AUTOSAR SWS Diagnostic Log and Trace (Classic Platform R22-11)** — spec (downloadable PDF)
   https://www.autosar.org/fileadmin/standards/R22-11/CP/AUTOSAR_SWS_DiagnosticLogAndTrace.pdf
   Why: Software Specification for the DLT module (basis of COVESA DLT protocol V2), covering module behaviour, configuration parameters and the Dlt header.
   Verified: 2026-09-24
   Archived: internet-docs/autosar-log-and-trace/classic-platform/AUTOSAR_SWS_DiagnosticLogAndTrace_R22-11.pdf

6. **AUTOSAR SWS Diagnostic Log and Trace (Classic Platform R19-11)** — spec (downloadable PDF)
   https://www.autosar.org/fileadmin/standards/R19-11/CP/AUTOSAR_SWS_DiagnosticLogAndTrace.pdf
   Why: The stable, widely adopted R19-11 specification that the COVESA DLT protocol V1 is based on — useful for matching existing implementations.
   Verified: 2026-09-24
   Archived: internet-docs/autosar-log-and-trace/classic-platform/AUTOSAR_SWS_DiagnosticLogAndTrace_R19-11.pdf

7. **COVESA dlt-daemon — Design Specification** — spec (Markdown, GitHub)
   https://github.com/COVESA/dlt-daemon/blob/master/doc/dlt_design_specification.md
   Why: Reference implementation's internal design spec; details message headers (storage/standard/extended), user & control messages, and daemon/library message flow.
   Verified: 2026-09-24
   Archived: internet-docs/dlt-protocol-specification/covesa-dlt-design-specification.md

8. **COVESA dlt-daemon — "DLT for Developers" Guide** — tutorial (Markdown, GitHub)
   https://github.com/COVESA/dlt-daemon/blob/master/doc/dlt_for_developers.md
   Why: Practical developer guide covering the libdlt API/macros, verbose vs. non-verbose logging, argument types, log levels, network trace and injection messages.
   Verified: 2026-09-24
   Archived: internet-docs/dlt-protocol-specification/covesa-dlt-for-developers.md

9. **COVESA dlt-daemon — Repository README / Overview** — repo (GitHub)
   https://github.com/COVESA/dlt-daemon
   Why: Canonical open-source implementation of the DLT protocol; documents V1/V2 protocol versions, tooling (dlt-receive, dlt-convert) and how the pieces fit together.
   Verified: 2026-09-24
   Archived: internet-docs/dlt-protocol-specification/covesa-dlt-daemon-repository-overview.md

10. **COVESA dlt-daemon — Documentation Site** — docs (web page)
    https://covesa.github.io/dlt-daemon/
    Why: Rendered documentation portal linking glossary, developer guide and advanced topics (LogStorage, MultiNode, network trace, filetransfer).
    Verified: 2026-09-24
    Archived: internet-docs/dlt-protocol-specification/covesa-dlt-daemon-documentation-portal.md

11. **Wireshark — DLT Display Filter Reference** — dissector reference (web page)
    https://www.wireshark.org/docs/dfref/d/dlt.html
    Why: Field-level reference for the DLT dissector — enumerates storage/standard/extended header fields and payload argument types, a compact cross-reference for parsing DLT.
    Verified: 2026-09-24
    Archived: internet-docs/dlt-protocol-specification/wireshark-dlt-display-filter-reference.md

12. **COVESA — Diagnostic Log & Trace Project Page** — docs (web page)
    https://covesa.global/project/diagnostic-log-trace/
    Why: Official COVESA project landing page describing DLT's purpose and its standardization in AUTOSAR — good high-level entry point.
    Verified: 2026-09-24
    Archived: internet-docs/dlt-protocol-specification/covesa-diagnostic-log-trace-project-page.md

### Adaptive Platform (Log and Trace / `ara::log`)

13. **AUTOSAR AP SWS Log and Trace (Adaptive Platform R25-11, latest)** — spec (downloadable PDF)
    https://www.autosar.org/fileadmin/standards/R25-11/AP/AUTOSAR_AP_SWS_LogAndTrace.pdf
    Why: Latest Adaptive Platform Software Specification for the Log and Trace functional cluster (`ara::log`) — API, severity levels, and DLT-based output to bus/console/file/ARTI-trace.
    Verified: 2026-09-28
    Archived: internet-docs/autosar-log-and-trace/adaptive-platform/AUTOSAR_AP_SWS_LogAndTrace_R25-11.pdf

14. **AUTOSAR AP SWS Log and Trace (Adaptive Platform R24-11)** — spec (downloadable PDF)
    https://www.autosar.org/fileadmin/standards/R24-11/AP/AUTOSAR_AP_SWS_LogAndTrace.pdf
    Why: R24-11 Adaptive Platform Software Specification for the Log and Trace functional cluster (`ara::log`) — API, severity levels, and DLT-based output to bus/console/file/ARTI-trace.
    Verified: 2026-09-24
    Archived: internet-docs/autosar-log-and-trace/adaptive-platform/AUTOSAR_AP_SWS_LogAndTrace_R24-11.pdf

15. **AUTOSAR AP SWS Log and Trace (Adaptive Platform R23-11)** — spec (downloadable PDF)
    https://www.autosar.org/fileadmin/standards/R23-11/AP/AUTOSAR_AP_SWS_LogAndTrace.pdf
    Why: R23-11 Adaptive Platform Log and Trace spec — adds tracing with modeled messages and interface for sending log messages; pairs with the Classic-side DLT protocol.
    Verified: 2026-09-24
    Archived: internet-docs/autosar-log-and-trace/adaptive-platform/AUTOSAR_AP_SWS_LogAndTrace_R23-11.pdf

16. **AUTOSAR AP SWS Log and Trace (Adaptive Platform R22-11)** — spec (downloadable PDF)
    https://www.autosar.org/fileadmin/standards/R22-11/AP/AUTOSAR_SWS_LogAndTrace.pdf
    Why: R22-11 Adaptive Platform Log and Trace spec — the `ara::log` logging framework and API definitions matching the R22-11 Classic DLT specs already archived.
    Verified: 2026-09-24
    Archived: internet-docs/autosar-log-and-trace/adaptive-platform/AUTOSAR_AP_SWS_LogAndTrace_R22-11.pdf

17. **AUTOSAR AP SWS Log and Trace (Adaptive Platform R19-11)** — spec (downloadable PDF)
    https://www.autosar.org/fileadmin/standards/R19-11/AP/AUTOSAR_SWS_LogAndTrace.pdf
    Why: The older R19-11 Adaptive Platform Log and Trace spec — provides parity with the R19-11 Classic DLT specs for comparing the early `ara::log` API surface.
    Verified: 2026-09-24
    Archived: internet-docs/autosar-log-and-trace/adaptive-platform/AUTOSAR_AP_SWS_LogAndTrace_R19-11.pdf

### Foundation — requirements & templates

18. **AUTOSAR FO RS Requirements on Log and Trace (Foundation R25-11, latest)** — spec (downloadable PDF)
    https://www.autosar.org/fileadmin/standards/R25-11/FO/AUTOSAR_FO_RS_LogAndTrace.pdf
    Why: Foundation requirements specification (Document ID 350) listing the high-level requirements the Log and Trace / Dlt solution must satisfy — the source requirements traced by the CP/AP specs.
    Verified: 2026-09-28
    Archived: internet-docs/autosar-log-and-trace/foundation/AUTOSAR_FO_RS_LogAndTrace_R25-11.pdf

19. **AUTOSAR FO TPS Log And Trace Extract Template (Foundation R25-11, latest)** — spec (downloadable PDF)
    https://www.autosar.org/fileadmin/standards/R25-11/FO/AUTOSAR_FO_TPS_LogAndTraceExtract.pdf
    Why: Foundation template specification (Document ID 1024) defining the Log and Trace Extract — the model/exchange format describing log sources (application/module) for non-verbose message decoding and tooling.
    Verified: 2026-09-28
    Archived: internet-docs/autosar-log-and-trace/foundation/AUTOSAR_FO_TPS_LogAndTraceExtract_R25-11.pdf

### Vendor / supplementary material

20. **Vector — MICROSAR Adaptive: Logging, Tracing and Monitoring Concept (User Day 2022)** — presentation (downloadable PDF)
    https://cdn.vector.com/cms/content/products/microsar/MICROSAR-UserDays/Presentations_2022/Vector_User_Day_2022_MICROSAR_Adaptive_Ziegler_Vector_Vehicle_Log_Trace.pdf
    Why: Vendor overview of AUTOSAR Adaptive logging/tracing — verbose API, LogLevels/Contexts and JSON-based configuration; practical context for the `ara::log` specs.
    Verified: 2026-09-24
    Archived: internet-docs/autosar-log-and-trace/vendor/Vector_MICROSAR_Adaptive_Log_Trace_2022.pdf

---
_20 links verified — Classic Platform: 3 AUTOSAR CP DLT specs (R19-11 → R25-11) + COVESA design spec, developer guide, repo/docs/project pages + Wireshark dissector reference; Adaptive Platform: 5 AP Log and Trace specs (R19-11 → R25-11); Foundation: RS Requirements + TPS Log and Trace Extract Template (R25-11); plus 1 Vector vendor presentation. All 20 archived offline under `internet-docs/`._
