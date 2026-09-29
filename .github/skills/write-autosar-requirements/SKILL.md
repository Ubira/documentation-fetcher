---
name: write-autosar-requirements
description: 'Turn a feature, system, or stakeholder prompt into clear, verifiable AUTOSAR-style requirements using the workspace requirement definition and template. Use when asked to derive, write, refine, or review requirements from prompt text.'
argument-hint: 'Requirement source prompt, plus optional ID prefix, AppliesTo platforms, and lifecycle state'
---

# Write AUTOSAR Requirements

Convert the user's source prompt into a set of atomic, verifiable requirements that follow the workspace's AUTOSAR requirement definition. Do not add behavior that is not supported by the prompt or other supplied context.

## Reference

Read [autosar-requirement-definition.md](../../../requirement-standardization/autosar-requirement-definition.md) before drafting. Its requirement template, sentence pattern, lifecycle guidance, obligation vocabulary, and `StandardNameEnum` are authoritative for this workflow.

## When to Use

- Derive requirements from a feature request, system description, stakeholder prompt, or use case.
- Refine vague requirements into clear, testable statements.
- Review a requirement set for conformance to the workspace template.

## Inputs

- **Source prompt** (required): the behavior, need, or problem from which requirements are to be derived.
- **Supporting context** (optional): definitions, constraints, interfaces, use cases, existing requirements, and references.
- **ID prefix or numbering scheme** (optional): preserve any scheme specified by the user or existing requirement set.
- **AppliesTo** (optional): one or more of `CP`, `AP`, or `FO`.
- **Lifecycle state** (optional): `VALID`, `DRAFT`, or `OBSOLETE`.

Ask a concise clarifying question only when an unknown changes the requirement meaning or makes a required field impossible to represent accurately. Otherwise proceed, mark unresolved fields `TBD`, and list the exact information needed. Never invent platform values, constraints, dependencies, or source facts.

## Procedure

1. **Read the governing definition.** Inspect the linked requirement definition and use its template and terminology. Treat the user's prompt and supplied project context as the source of behavioral facts.

2. **Extract candidate behaviors.** Identify the actors or system elements, required outcomes, triggering events or static conditions, constraints, exceptions, and stated rationale. Separate distinct behaviors into separate candidates. Do not turn explanations, goals, or suggestions into mandatory behavior unless the source makes them requirements.

3. **Resolve ambiguity and scope.** Check whether each candidate has a clear subject and an observable outcome. Ask about ambiguities that would lead to materially different implementations; otherwise retain the uncertainty as `TBD` rather than silently choosing an interpretation. Preserve scope and strength from the source.

4. **Write verifiable statements.** Use the standard's pattern: optional `If` or `When` condition, followed by a subject, `shall`, and a statement that can be verified or falsified. Use `when` for an event and `if` for a static condition. Keep each requirement atomic and specific enough to verify. Use `shall` for an absolute requirement; use `should` or `may` only when the source expresses a recommendation or option. Avoid vague terms such as "appropriate", "fast", or "user-friendly" unless the source defines measurable criteria.

5. **Assign identifiers and lifecycle.** Preserve supplied IDs and established project numbering. If no scheme exists, use unique provisional IDs `REQ_0001`, `REQ_0002`, and so on, and identify them as provisional. Use `VALID` by default when no lifecycle state is supplied, as the standard defines this as the default. Use `DRAFT` only for explicitly experimental requirements. Use `OBSOLETE` only when the requirement is explicitly obsolete, and state its recommended alternative in the rationale or an accompanying note.

6. **Complete the template fields.** Give each requirement a unique short text for its long name and fill the fields below. Keep rationale and use case grounded in the supplied context. List only explicit dependencies and supporting references. Use `-` when a field is intentionally empty; use `TBD` when information is needed but unavailable. `AppliesTo` accepts only `SPA2`, `SPA3`, and `SPA3x`; do not infer a value from general AUTOSAR context.

7. **Check quality and deliver.** Review every statement against the checklist below. Return the requirements in Markdown using the template field names. Follow the user's requested file destination if provided; otherwise present the result in the response and ask before creating a new requirements document.

## Output Template

Create one table per requirement, using this field order:

| Field | Value |
| --- | --- |
| **ID (shortName)** | `REQ_0001` |
| **LifeCycleState (Type)** | `VALID` |
| **Unique Short Text (longName)** | Concise requirement headline |
| **Description** | The <subject> shall <verifiable statement>. |
| **Rationale** | Grounded justification, or `-` |
| **AppliesTo** | `SPA2`, `SPA3`, and/or `SPA3x`, or `TBD` |
| **Use Case** | Grounded use case, or `-` |
| **Dependencies** | Explicit requirement references, or `-` |
| **Supporting Material** | Supplied references, or `-` |

When useful, add a brief **Open Questions and Assumptions** section after the tables. Keep assumptions distinct from requirement statements. Do not add the source prompt as a supporting reference unless it is available as a stable reference and the user wants trace links.

## Quality Checklist

- [ ] Every requirement has a unique ID and a concise, distinct headline.
- [ ] Every description is a complete English sentence with a clear subject and obligation keyword.
- [ ] Every description is atomic and objectively verifiable or falsifiable.
- [ ] Conditions distinguish static `if` from event-based `when` and use `then` where appropriate.
- [ ] Obligation strength matches the source; no new mandatory behavior has been inferred.
- [ ] Lifecycle state follows the standard; `VALID` is the default when unspecified.
- [ ] `AppliesTo` contains only `SPA2`, `SPA3`, or `SPA3x`, or is explicitly marked `TBD`.
- [ ] Rationale, use case, dependencies, and supporting material are grounded in supplied information.
- [ ] Unknowns are visible as `TBD` or open questions rather than presented as facts.
- [ ] The output follows the requirement definition's template and requested destination.