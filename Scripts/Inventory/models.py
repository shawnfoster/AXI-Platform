"""
AXI Inventory Engine - Data Models
Module: models.py
Project: AXI-ENG-001
Version: 1.0.0
"""

from dataclasses import dataclass, asdict
from pathlib import Path
from datetime import datetime

@dataclass
class InventoryRecord:
    inventory_id: str
    filename: str
    extension: str
    relative_path: str
    repository: str
    file_size: int
    last_modified: str
    source_package: str = ""
    object_type: str = "Unknown"
    version: str = ""
    checksum: str = ""
    duplicate_candidate: bool = False
    review_required: bool = False
    lifecycle: str = "Discovered"
    status: str = "Inventory"
    notes: str = ""

    @classmethod
    def from_path(cls, inventory_id: str, root: Path, file_path: Path):
        stat = file_path.stat()
        return cls(
            inventory_id=inventory_id,
            filename=file_path.name,
            extension=file_path.suffix.lower(),
            relative_path=str(file_path.relative_to(root)),
            repository=root.name,
            file_size=stat.st_size,
            last_modified=datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
        )

    def to_dict(self):
        return asdict(self)


if __name__ == "__main__":
    root = Path.cwd()
    sample = InventoryRecord.from_path("INV-000001", root, Path(__file__))
    print(sample.to_dict())
