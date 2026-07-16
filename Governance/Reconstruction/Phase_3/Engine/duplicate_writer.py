import csv
import json
from pathlib import Path

OUTDIR = Path("Governance/Reconstruction/Phase_3/Duplicates")

OUTDIR.mkdir(parents=True, exist_ok=True)

def write_duplicate_register(groups):

    rows = []

    for sha, items in groups.items():
        gid = sha[:12]

        for item in items:
            rows.append({
                "duplicate_group": gid,
                "sha256": sha,
                "artifact_id": item["artifact_id"],
                "filename": item["filename"],
                "relative_path": item["relative_path"]
            })

    fields = [
        "duplicate_group",
        "sha256",
        "artifact_id",
        "filename",
        "relative_path"
    ]

    with open(
        OUTDIR/"AXI-REG-002_Duplicate_Register.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    with open(
        OUTDIR/"AXI-REG-002_Duplicate_Register.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(rows, f, indent=2)

    summary = {
        "duplicate_groups": len(groups),
        "duplicate_files": len(rows)
    }

    with open(
        OUTDIR/"duplicate_summary.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(summary, f, indent=2)

    with open(
        OUTDIR/"duplicate_log.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write("Duplicate Resolution completed successfully.\n")
