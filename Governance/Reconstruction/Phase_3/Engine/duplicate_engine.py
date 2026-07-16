#!/usr/bin/env python3
"""
AXI Duplicate Resolution Engine
Engine ID: AXI-ENG-003
Version: 1.0.0
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from duplicate_writer import write_duplicate_register

INVENTORY = Path(
    "Governance/Reconstruction/Phase_3/Inventory/"
    "AXI-REG-001_Artifact_Inventory.json"
)

def load_inventory():
    with INVENTORY.open("r", encoding="utf-8") as f:
        return json.load(f)

def find_duplicates(records):
    groups = defaultdict(list)

    for record in records:
        groups[record["sha256"]].append(record)

    duplicates = {
        sha: items
        for sha, items in groups.items()
        if len(items) > 1
    }

    return duplicates

def main():

    if not INVENTORY.exists():
        print(f"ERROR: Missing inventory file:\n{INVENTORY}")
        return 1

    records = load_inventory()

    duplicates = find_duplicates(records)

    duplicate_files = sum(len(v) for v in duplicates.values())

    write_duplicate_register(duplicates)

    print()
    print("AXI Duplicate Resolution Engine")
    print("--------------------------------")
    print(f"Artifacts scanned : {len(records)}")
    print(f"Duplicate groups  : {len(duplicates)}")
    print(f"Duplicate files   : {duplicate_files}")
    print("Register written successfully.")

    return 0 

if __name__ == "__main__":
    raise SystemExit(main())
