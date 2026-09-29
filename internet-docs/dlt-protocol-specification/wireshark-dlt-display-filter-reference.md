# Wireshark — Diagnostic Log and Trace (DLT) Display Filter Reference

> **Source:** https://www.wireshark.org/docs/dfref/d/dlt.html
> **Fetched:** 2026-09-24
> **Author / Publisher:** Wireshark Foundation
> **Type:** protocol dissector reference
> **Tags:** dlt, wireshark, dissector, display-filter, autosar, protocol-fields, header

## Summary

The Wireshark display-filter reference for the DLT dissector (protocol field name `dlt`, versions 3.2.0 to 4.6.9). It enumerates every field Wireshark decodes from a DLT message, which effectively documents the on-the-wire structure of the DLT protocol: storage header, standard/base header (header type flags, message counter, length, ECU/session IDs, timestamp), extended header (message info, number of arguments, application/context IDs), the typed payload arguments, and control-service message fields. Useful as a compact, field-level cross-reference when parsing or debugging DLT traffic.

## Key Concepts

- **Header Type (`dlt.header_type`)** flags: `version`, `msb_first` (MSB First / big-endian payload), `with_ecu_id`, `with_session_id` (3.4.0+), `with_timestamp`, `ext_header` (extended header present).
- **Standard/base header fields**: `dlt.msg_counter`, `dlt.length`, `dlt.ecu_id`, `dlt.session_id`, `dlt.timestamp`.
- **Extended header / message info** (`dlt.msg_info`): `msg_type`, `msg_type_info`, `verbose`; plus `dlt.num_of_args`, `dlt.application_id`, `dlt.context_id`, `dlt.message_id` (non-verbose).
- **Storage header** (4.2.0+): `dlt.storage.ecu_name`, `dlt.storage.timestamp_s`, `dlt.storage.timestamp_us`, `dlt.storage.reserved`.
- **Payload** (`dlt.payload`, `dlt.payload.data`) and typed verbose arguments under `dlt.data.*`.
- **Control-service fields** under `dlt.service.*` (log level, trace status, descriptions, SW-version, etc.).

## Details

### Header / framing fields

| Field name | Description | Type | Versions |
| --- | --- | --- | --- |
| `dlt.header_type` | Header Type | Label | 3.2.0–4.6.9 |
| `dlt.header_type.version` | Version | uint8 | 3.2.0–4.6.9 |
| `dlt.header_type.msb_first` | MSB First | Boolean | 3.2.0–4.6.9 |
| `dlt.header_type.with_ecu_id` | With ECU ID | Boolean | 3.2.0–4.6.9 |
| `dlt.header_type.with_session_id` | With Session ID | Boolean | 3.4.0–4.6.9 |
| `dlt.header_type.with_timestamp` | With Timestamp | Boolean | 3.2.0–4.6.9 |
| `dlt.header_type.ext_header` | Extended Header | Boolean | 3.2.0–4.6.9 |
| `dlt.msg_counter` | Message Counter | uint8 | 3.2.0–4.6.9 |
| `dlt.length` | Length | uint16 | 3.2.0–4.6.9 |
| `dlt.ecu_id` | ECU ID | string | 3.2.0–4.6.9 |
| `dlt.session_id` | Session ID | uint32 | 3.2.0–4.6.9 |
| `dlt.timestamp` | Timestamp | double | 3.2.0–4.6.9 |
| `dlt.ext_header` | Extended Header | Label | 3.2.0–4.6.9 |

### Message info / identity

| Field name | Description | Type | Versions |
| --- | --- | --- | --- |
| `dlt.msg_info` | Message Info | Label | 3.2.0–4.6.9 |
| `dlt.msg_info.msg_type` | Message Type | uint8 | 3.2.0–4.6.9 |
| `dlt.msg_info.msg_type_info` | Message Type Info | uint8 | 3.2.0–4.6.9 |
| `dlt.msg_info.verbose` | Verbose | Boolean | 3.2.0–4.6.9 |
| `dlt.num_of_args` | Number of Arguments | uint8 | 3.2.0–4.6.9 |
| `dlt.application_id` | Application ID | string | 3.2.0–4.6.9 |
| `dlt.context_id` | Context ID | string | 3.2.0–4.6.9 |
| `dlt.message_id` | Message ID | uint32 | 3.2.0–4.6.9 |

### Storage header (pcap/file)

| Field name | Description | Type | Versions |
| --- | --- | --- | --- |
| `dlt.storage.ecu_name` | ECU Name | string | 4.2.0–4.6.9 |
| `dlt.storage.timestamp_s` | Timestamp s | uint32 | 4.2.0–4.6.9 |
| `dlt.storage.timestamp_us` | Timestamp us | uint32 | 4.2.0–4.6.9 |
| `dlt.storage.reserved` | Reserved | bytes | 4.2.0–4.6.9 |

### Verbose payload argument types (`dlt.data.*`)

`bool`, `int8/16/32/64`, `uint8/16/32/64`, `float` (single), `double`, `string`, `rawd` (byte sequence).

### Control service fields (`dlt.service.*`)

`application_id`, `context_id`, `app_description`, `ctx_description`, `appid_log_levels`, `log_level`, `new_log_level`, `trace_status`, `new_trace_status`, `new_status`, `count`, `length`, `options`, `status`, `res` (reserved), `sw_version`.

### Error / diagnostic labels

`dlt.buffer_too_short`, `dlt.parsing_error`, `dlt.unsupported_datatype`, `dlt.unsupported_length_datatype`, `dlt.unsupported_non_verbose_message_type`, `dlt.unsupported_string_coding`.

## References

- Wireshark Display Filter Reference index: https://www.wireshark.org/docs/dfref/
- AUTOSAR Log and Trace Protocol Specification: https://www.autosar.org/fileadmin/standards/R22-11/FO/AUTOSAR_PRS_LogAndTraceProtocol.pdf
- COVESA dlt-daemon design spec: https://github.com/COVESA/dlt-daemon/blob/master/doc/dlt_design_specification.md

---
_Captured from https://www.wireshark.org/docs/dfref/d/dlt.html on 2026-09-24. Content belongs to its original author(s) (Wireshark Foundation)._
