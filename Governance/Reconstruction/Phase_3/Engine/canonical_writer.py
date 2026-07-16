import csv
import json
from pathlib import Path

OUTDIR = Path("Governance/Reconstruction/Phase_3/Canon")
OUTDIR.mkdir(parents=True, exist_ok=True)


def write_canonical_register(rows):

    fields = [
        "duplicate_group",
        "recommended_artifact",
        "confidence",
        "classification",
        "relative_path",
        "reason",
        "status"
    ]

    with open(
        OUTDIR / "AXI-REG-005_Canonical_Register.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    with open(
        OUTDIR / "AXI-REG-005_Canonical_Register.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(rows, f, indent=2)

    summary = {
        "recommendations": len(rows),
        "status": "Operational"
    }

    with open(
        OUTDIR / "canonical_summary.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(summary, f, indent=2)

    with open(
        OUTDIR / "canonical_log.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write("Canonical Selection completed successfully.\n")