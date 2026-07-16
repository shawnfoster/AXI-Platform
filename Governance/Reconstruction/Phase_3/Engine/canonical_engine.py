#!/usr/bin/env python3

import json
from pathlib import Path

from canonical_writer import write_canonical_register

PROVENANCE = Path(
    "Governance/Reconstruction/Phase_3/Provenance/AXI-REG-004_Provenance_Register.json"
)


def load():
    with PROVENANCE.open("r", encoding="utf-8") as f:
        return json.load(f)


def score(record):

    score = 50

    path = record["relative_path"].lower()

    if "/canon/" in path:
        score += 30

    if "/archive/" in path:
        score -= 20

    if "draft" in path:
        score -= 15

    if record["relationship"] == "Unique":
        score += 5

    return score


def main():

    provenance = load()

    groups = {}

    for record in provenance:

        if record["duplicate_count"] <= 1:
            continue

        groups.setdefault(
            record["duplicate_group"],
            []
        ).append(record)

    recommendations = []

    for group, rows in groups.items():

        winner = max(rows, key=score)

        recommendations.append({

            "duplicate_group": group,
            "recommended_artifact": winner["artifact_id"],
            "confidence": score(winner),
            "classification": winner["classification"],
            "relative_path": winner["relative_path"],
            "reason": "Highest evidence score",
            "status": "Recommended"

        })

    write_canonical_register(recommendations)

    print()
    print("AXI Canonical Selection Engine")
    print("--------------------------------")
    print(f"Duplicate Groups : {len(groups)}")
    print(f"Recommendations  : {len(recommendations)}")
    print("Canonical Register written successfully.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())