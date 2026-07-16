#!/usr/bin/env python3

import json
from pathlib import Path

from provenance_writer import write_provenance_register

INVENTORY = Path(
    "Governance/Reconstruction/Phase_3/Inventory/AXI-REG-001_Artifact_Inventory.json"
)

CLASSIFICATION = Path(
    "Governance/Reconstruction/Phase_3/Classification/AXI-REG-003_Artifact_Classification.json"
)

DUPLICATES = Path(
    "Governance/Reconstruction/Phase_3/Duplicates/AXI-REG-002_Duplicate_Register.json"
)


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    inventory = load(INVENTORY)
    classification = load(CLASSIFICATION)
    duplicates = load(DUPLICATES)

    class_map = {
        r["artifact_id"]: r.get("classification", "Unknown")
        for r in classification
    }

    dup_map = {}

    for row in duplicates:
        group = row["duplicate_group"]

        dup_map.setdefault(group, [])

        dup_map[group].append(row["artifact_id"])

    artifact_lookup = {}

    for group, ids in dup_map.items():
        for aid in ids:
            artifact_lookup[aid] = (
                group,
                len(ids)
            )

    rows = []

    for item in inventory:

        group, count = artifact_lookup.get(
            item["artifact_id"],
            ("", 1)
        )

        rows.append({

            "artifact_id": item["artifact_id"],
            "sha256": item["sha256"],
            "relative_path": item["relative_path"],
            "classification": class_map.get(
                item["artifact_id"],
                "Unknown"
            ),
            "duplicate_group": group,
            "duplicate_count": count,
            "relationship": (
                "Duplicate" if count > 1 else "Unique"
            ),
            "confidence": 1.0,
            "status": "Observed"

        })

    write_provenance_register(rows)

    print()
    print("AXI Provenance Engine")
    print("---------------------")
    print(f"Artifacts : {len(rows)}")
    print("Register written successfully.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())