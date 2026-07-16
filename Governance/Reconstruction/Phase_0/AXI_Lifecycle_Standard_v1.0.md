# AXI Lifecycle Standard v1.0

**Document ID:** AXI-LS-001  
**Version:** 1.0  
**Status:** Founder Review  
**Lifecycle:** Draft

## Purpose
Define the lifecycle states that every governed AXI object shall follow from creation through archival while preserving governance, provenance, and traceability.

## Guiding Principles
1. Every governed object shall have exactly one current lifecycle state.
2. Lifecycle transitions shall be recorded.
3. No object may bypass required approval gates.
4. Superseded objects remain preserved for historical traceability.

## Lifecycle States

### Draft
Initial working version under development.

### Under Review
Submitted for structured review. Changes may occur.

### Candidate
Review complete and awaiting Founder decision.

### Approved
Authorized as the current canonical version.

### Active
Approved and in operational use.

### Superseded
Replaced by a newer approved object. Retained for history.

### Deprecated
Retained temporarily but scheduled for retirement.

### Archived
Preserved for historical reference only.

### Reference Only
Informational object that is not canonical.

### Rejected
Rejected during review. Retained with rationale.

## Allowed Transitions

Draft → Under Review  
Under Review → Candidate  
Candidate → Approved or Rejected  
Approved → Active  
Active → Superseded or Deprecated  
Deprecated → Archived

## Transition Requirements

Every transition shall record:
- Previous state
- New state
- Date
- Authority
- Rationale
- Supporting decision reference

## Validation Rules
An object may not enter Approved or Active unless:
- Required metadata is complete.
- Provenance is complete.
- Identifier is valid.
- Required approvals are recorded.

## Definition of Completion
This standard is satisfied when every governed object has a valid lifecycle state and every state transition is auditable.

---
Next Document: AXI-PP-001 Provenance Policy
