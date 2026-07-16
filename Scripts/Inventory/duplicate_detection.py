
"""
AXI Inventory Engine - Duplicate Detection
Module: duplicate_detection.py
Project: AXI-ENG-001
Version: 1.0.0
"""

from collections import defaultdict

def detect_duplicates(records):
    """Classify duplicate candidates from InventoryRecord objects."""
    by_hash = defaultdict(list)
    by_name_size = defaultdict(list)

    for record in records:
        checksum = getattr(record, "checksum", "")
        if checksum:
            by_hash[checksum].append(record)

        key = (record.filename.lower(), record.file_size)
        by_name_size[key].append(record)

    results = {
        "exact": [],
        "strong": []
    }

    for checksum, group in by_hash.items():
        if checksum and len(group) > 1:
            results["exact"].append(group)

    for key, group in by_name_size.items():
        if len(group) > 1:
            results["strong"].append(group)

    return results


if __name__ == "__main__":
    print("Duplicate Detection Module Ready")
    print("Import detect_duplicates(records) from inventory_engine.py")
