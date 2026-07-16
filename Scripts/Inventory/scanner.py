"""
AXI Inventory Engine - Scanner
"""
from pathlib import Path
from models import InventoryRecord

SKIP_DIRS={".git","__pycache__",".venv"}
SKIP_FILES={".DS_Store"}

def scan_repository(root: Path):
    records=[]
    counter=1
    for path in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_dir():
            continue
        if path.name in SKIP_FILES:
            continue
        rec=InventoryRecord.from_path(f"INV-{counter:06d}",root,path)
        records.append(rec)
        counter+=1
    return records

if __name__=="__main__":
    repo=Path.cwd()
    records=scan_repository(repo)
    print(f"Scanned {len(records)} files.")
    if records:
        print(records[0].to_dict())
