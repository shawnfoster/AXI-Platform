import csv
import json
from pathlib import Path

OUTDIR = Path("Governance/Reconstruction/Phase_3/Provenance")
OUTDIR.mkdir(parents=True, exist_ok=True)


def write_provenance_register(rows):

    fields = [
        "artifact_id",
        "sha256",
        "relative_path",
        "classification",
        "duplicate_group",
        "duplicate_count",
        "relationship",
        "confidence",
        "status"
    ]

    with open(
        OUTDIR / "AXI-REG-004_Provenance_Register.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    with open(
        OUTDIR / "AXI-REG-004_Provenance_Register.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(rows, f, indent=2)

    summary = {
        "artifacts": len(rows),
        "duplicate_artifacts": sum(
            1 for r in rows if r["duplicate_count"] > 1
        )
    }

    with open(
        OUTDIR / "provenance_summary.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(summary, f, indent=2)

    with open(
        OUTDIR / "provenance_log.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write("Provenance generation completed successfully.\n")