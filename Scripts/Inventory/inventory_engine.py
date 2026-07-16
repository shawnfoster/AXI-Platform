"""
AXI Inventory Engine
Module: inventory_engine.py
Project: AXI-ENG-001
Version: 1.1.0
"""

import sys

from config import load_config
from scanner import scan_repository
from hashing import sha256_file
from duplicate_detection import detect_duplicates
from writers import write_csv, write_xlsx


def main() -> int:
    cfg = load_config()

    records = scan_repository(cfg.repository_root)

    for record in records:
        try:
            record.checksum = sha256_file(cfg.repository_root / record.relative_path)
        except Exception as exc:
            record.review_required = True
            record.notes = f"Hash error: {exc}"

    duplicates = detect_duplicates(records)

    write_xlsx(records, cfg.inventory_workbook)
    write_csv(records, cfg.inventory_csv)

    print("=" * 60)
    print("AXI Inventory Engine v1.1.0")
    print("=" * 60)
    print(f"Repository      : {cfg.repository_root}")
    print(f"Files           : {len(records)}")
    print(f"Exact Duplicates: {len(duplicates['exact'])}")
    print(f"Strong Matches  : {len(duplicates['strong'])}")
    print(f"Workbook        : {cfg.inventory_workbook}")
    print(f"CSV             : {cfg.inventory_csv}")
    print("Status          : SUCCESS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
