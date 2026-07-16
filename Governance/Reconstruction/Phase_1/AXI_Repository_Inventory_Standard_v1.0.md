# AXI Repository Inventory Standard v1.0

**Document ID:** AXI-INV-001  
**Version:** 1.0  
**Status:** Founder Review  
**Lifecycle:** Draft

## Purpose
Establish the governed standard for inventorying all AXI source artifacts before any analysis, reconstruction, or canonization.

## Scope
This standard applies to every file, folder, archive, dataset, image, document, spreadsheet, presentation, script, and repository included in the AXI corpus.

## Inventory Principles
1. Inventory precedes interpretation.
2. Inventory shall not modify source artifacts.
3. Every source receives a unique inventory record.
4. Duplicate candidates are recorded, not merged.
5. Unknown items remain classified as Unknown until reviewed.

## Required Inventory Fields
- Inventory ID
- Filename
- Extension
- Relative Path
- Repository
- File Size
- Last Modified Date
- Source Package
- Object Type (if known)
- Version (if known)
- Hash/Checksum (when available)
- Duplicate Candidate (Yes/No)
- Review Required (Yes/No)
- Notes

## Inventory Workflow
1. Discover artifact.
2. Register inventory record.
3. Capture metadata.
4. Classify format.
5. Flag duplicate candidates.
6. Flag review-required items.
7. Preserve without modification.
8. Publish inventory register.

## Validation Rules
An inventory is complete only when every discovered artifact has a unique record and required metadata.

## Outputs
- Repository Inventory Register
- Duplicate Candidate Register
- Review Queue
- Inventory Summary Report

## Definition of Done
This standard is satisfied when every artifact in scope has been inventoried without altering the original corpus.

---
Next Document: AXI-INV-002 Repository Inventory Register
