# From AUTOSAR_FO_TPS_StandardizationTemplate.pdf

## Relevant Requirements
[TPS_STDT_00078] Representation of requirements in AUTOSAR documents
⌈AUTOSAR requirements are represented using the structure of [TPS_STDT_00060]
where the following attributes are presented as a table:

• The headline shall contain the Id (shortName), the LifeCycleState (type)
and a unique short text (longName) of the requirement.

• The value of Type shall be one of "valid", "draft" or "obsolete", see
[TPS_STDT_00064].

• The description of requirement contains of a complete English sentence using
the sentence pattern [TPS_STDT_00094] including one of the keywords from
[TPS_STDT_00053]. Additional information: needed to understand the requirement,
can be added to the description.

• The rationale can be used to justify or rationalize the requirement.

• Use case can be used to describe the use case of the requirement.

• Applies to shall contain a comma separated tag list with one of the following
values from StandardNameEnum.

• Dependencies may contain references to other requirements in this document
which this requirement depends on.

• Supporting material can be used for documenting references to other documents
or models that support the implementation of this requirement.
⌋

[TPS_STDT_00064] Applied Life Cycle Information Sets on AUTOSAR provided
Models (M1) ⌈The following LifeCycleStates are applied for AUTOSAR provided
model elements:

• VALID: This indicates that the related entity is a valid part of the document. This
is the default.

• DRAFT: This indicates that the related entity is introduced newly in the model
but still experimental. This information is published but is subject to be changed
without backward compatibility management.

• OBSOLETE: This indicates that the related entity is obsolete and kept in the model
for compatibility reasons. If this tag is set, the note shall express the recommended
alternative solution.

• REMOVED: This indicates that the related entity is removed from the model. It
shall not be used and should not even appear in documents. An AUTOSAR
release does not contain such elements. It is intended for AUTOSAR internal development.

Even if such removed elements are not included in an .arxml they can still be
referenced in a LifeCycleInfoSet by using the ≪atpUriDef≫ attribute of
type Referrable: lcObject, respectively useInstead.
If an object is not referenced in a LifeCycleInfoSet, the related entity is a valid part
of the current model.⌋

Note that according to [TPS_STDT_00064] if there is no life cycle information for an
element then it is defined that the element is valid. In other words, in general there
is no need to define a LifeCycleInfoSet with defaultLcState=VALID. Nevertheless,
there might be use cases when it could be useful to explicitly define such a
LifeCycleInfoSet. For example if element "x" gets LifeCycleState=OBSOLETE
and subsequently this is identified as an error and the life cycle returns back to VALID.
This could be documented in such a LifeCycleInfoSet.
An ARXML representation of the life cycle according is provided with [TPS_GST_-
00051].

[TPS_STDT_00094] Sentence pattern ⌈The sentence pattern is built up by:

• < OptionalCondition >: A condition under which the < Statement > shall be
true. The condition starts with either if or when and ends with then. Where
when identifies an event. I.e. the point in time when the condition becomes
true. In natural language you could use "as soon as" to express the same. If
in contrast identifies a static condition which is independent from time. For static
conditions you may add else (optionally) after the < Statement > to express an
alternative requirement by appending it as an additional sentence following the
pattern.

• < Subject >: The item that is to fulfill the < Statement >. Remark: The subject
typically represents your subject under development, a property or a part of it. It
is highly recommended to maintain an overview of the subjects you are specifying
in the introductory section of your specification document.

• shall: Separates the < Subject > from the < Statement > and identifies (partial)
requirements.

• < Statement >: A statement that can either be verified or falsified. If the statement
is true, then the < Subject > satisfies the requirement, otherwise it does
not.
⌋

[TPS_STDT_00053] Expression of obligation ⌈The following verbal forms for the
expression of obligation shall be used to indicate requirements.
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as follows.
Note that the requirement level of the document in which they are used modifies the
force of these words.

• MUST: This word, or the adjective "LEGALLY REQUIRED", means that the definition
is an absolute requirement of the specification due to legal issues.

• MUST NOT: This phrase, or the phrase "MUST NOT", means that the definition
is an absolute prohibition of the specification due to legal issues.

• SHALL: This phrase, or the adjective "REQUIRED", means that the definition is
an absolute requirement of the specification.

• SHALL NOT: This phrase means that the definition is an absolute prohibition of
the specification.

• SHOULD: This word, or the adjective "RECOMMENDED", means that there may
exist valid reasons in particular circumstances to ignore a particular item, but the
full implications must be understood and carefully weighed before choosing a
different course.

• SHOULD NOT: This phrase, or the phrase "NOT RECOMMENDED", means that
there may exist valid reasons in particular circumstances when the particular behavior
is acceptable or even useful, but the full implications should be understood
and the case carefully weighed before implementing any behavior described with
this label.

• MAY: This word, or the adjective "OPTIONAL", means that an item is truly optional.
One vendor may choose to include the item because a particular marketplace
requires it or because the vendor feels that it enhances the product while
another vendor may omit the same item.
An implementation, which does not include a particular option, SHALL be prepared
to interoperate with another implementation, which does include the option, though
perhaps with reduced functionality. In the same vein an implementation, which does
include a particular option, SHALL be prepared to interoperate with another implementation,
which does not include the option (except, of course, for the feature the option
provides.)⌋

[TPS_STDT_00060] StructuredReq ⌈This represents a structured requirement as it
is used within AUTOSAR RS documents.⌋

## Table B.93: StructuredReq

| Class | StructuredReq | | | |
| --- | --- | --- | --- | --- |
| **Note** | This represents a structured requirement. This is intended for a case where specific requirements for features are collected. Note that this can be rendered as a labeled list. | | | |
| **Base** | ARObject, DocumentViewSelectable, Identifiable, MultilanguageReferrable, Paginateable, Referrable, Traceable | | | |
| **Aggregated by** | DocumentationBlock.structuredReq | | | |
| **Attribute** | **Type** | **Mult.** | **Kind** | **Note** |
| appliesTo | StandardNameEnum | * | attr | This attribute represents the platform the requirement is assigned to. Tags: xml.namePlural=APPLIES-TO-DEPENDENCIES; xml.sequenceOffset=25 |
| conflicts | DocumentationBlock | 0..1 | aggr | This represents an informal specification of conflicts. Tags: xml.sequenceOffset=40 |
| date | DateTime | 1 | attr | This represents the date when the requirement was initiated. Tags: xml.sequenceOffset=5 |
| dependencies | DocumentationBlock | 0..1 | aggr | This represents an informal specification of dependencies. Note that upstream tracing should be formalized in the property trace provided by the superclass Traceable. Tags: xml.sequenceOffset=30 |
| description | DocumentationBlock | 0..1 | aggr | This represents the general description of the requirement. Tags: xml.sequenceOffset=10 |
| importance | String | 1 | attr | This allows to represent the importance of the requirement. Tags: xml.sequenceOffset=8 |
| issuedBy | String | 1 | attr | This represents the person, organization or authority which issued the requirement. Tags: xml.sequenceOffset=6 |
| rationale | DocumentationBlock | 0..1 | aggr | This represents the rationale of the requirement. Tags: xml.sequenceOffset=20 |
| remark | DocumentationBlock | 0..1 | aggr | This represents an informal remark. Note that this is not modeled as annotation, since these remark is still essential part of the requirement. Tags: xml.sequenceOffset=60 |
| supportingMaterial | DocumentationBlock | 0..1 | aggr | This represents an informal specification of the supporting material. Tags: xml.sequenceOffset=50 |
| testedItem | Traceable | * | ref | This association represents the ability to trace on the same specification level. This supports for example the of acceptance tests. Tags: xml.sequenceOffset=70 |
| type | String | 1 | attr | This attribute allows to denote the type of requirement to denote for example is it an "enhancement", "new feature" etc. Tags: xml.sequenceOffset=7 |
| useCase | DocumentationBlock | 0..1 | aggr | This describes the relevant use cases. Note that formal references to use cases should be done in the trace relation. Tags: xml.sequenceOffset=35 |

## StandardNameEnum
|  |  |
| --- | --- |
| **Enumeration** | StandardNameEnum |
| **Note** | This enumeration lists all allowed standard abbreviations |
| **Literal** | SPA2, SPA3, SPA3x |

# Requirement Template
|  |  |
| --- | --- |
| **ID (shortName)** | This specifies an identifying shortName for the object. It needs to be unique within its context and is intended for humans but even more for technical reference |
| **LifeCycleState (Type)** | The value of Type shall be one of "valid", "draft" or "obsolete" |
| **Unique Short Text (longName)** | This specifies the long name of the object. Long name is targeted to human readers and acts like a headline |
| **Description** | The description of requirement contains of a complete English sentence using the sentence pattern [TPS_STDT_00094] including one of the keywords from [TPS_STDT_00053]. Additional information: needed to understand the requirement, can be added to the description |
| **Rationale** | The rationale can be used to justify or rationalize the requirement |
| **AppliesTo** | Applies to shall contain a comma separated tag list with one of the following values from StandardNameEnum |
| **Use Case** | Use case can be used to describe the use case of the requirement |
| **Dependencies** | Dependencies may contain references to other requirements in this document which this requirement depends on |
| **Supporting Material** | Supporting material can be used for documenting references to other documents or models that support the implementation of this requirement |


## Requirement Example

This example is taken from AUTOSAR documentation, so the AppliesTo field doesn't show consistent values.

|  |  |
| --- | --- |
| **ID (shortName)** | RS_LT_00047 |
| **LifeCycleState (Type)** | VALID |
| **Unique Short Text (longName)** | Logging shall support initialization and registration |
| **Description** | Logging shall support to initialize the logging framework and to register the source of logging information |
| **Rationale** | To be able to filter and associate logging information with the origin, it is necessary that applications register themselves at the logging framework |
| **AppliesTo** | CP,AP |
| **Use Case** | Associate logging information with the origin, apply filter settings and provide additional information |
| **Dependencies** | - |
| **Supporting Material** | - |