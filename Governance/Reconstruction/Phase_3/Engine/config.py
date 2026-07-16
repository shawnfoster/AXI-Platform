from dataclasses import dataclass
from pathlib import Path
@dataclass
class Config:
    repository_root: Path
    inventory_dir: Path
def load_config(root: Path)->Config:
    inv=root/'Governance'/'Reconstruction'/'Phase_3'/'Inventory'
    inv.mkdir(parents=True, exist_ok=True)
    return Config(root,inv)
