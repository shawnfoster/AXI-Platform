"""
AXI Inventory Engine - Configuration
Module: config.py
Project: AXI-ENG-001
Version: 1.0.0
"""

from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class InventoryConfig:
    repository_root: Path
    reconstruction_root: Path
    phase1_root: Path
    inventory_dir: Path
    registers_dir: Path
    reports_dir: Path
    logs_dir: Path
    inventory_workbook: Path
    inventory_csv: Path
    log_file: Path

def discover_repository_root(start=None):
    current=(start or Path.cwd()).resolve()
    for candidate in [current,*current.parents]:
        if (candidate/'Governance').exists() and (candidate/'Scripts').exists():
            return candidate
    raise FileNotFoundError('Unable to locate AXI repository root.')

def load_config(start=None):
    root=discover_repository_root(start)
    reconstruction=root/'Governance'/'Reconstruction'
    phase1=reconstruction/'Phase_1'
    return InventoryConfig(
        repository_root=root,
        reconstruction_root=reconstruction,
        phase1_root=phase1,
        inventory_dir=phase1/'Inventory',
        registers_dir=phase1/'Registers',
        reports_dir=phase1/'Reports',
        logs_dir=phase1/'Logs',
        inventory_workbook=phase1/'Registers'/'AXI_Repository_Inventory_Register_v1.0.xlsx',
        inventory_csv=phase1/'Registers'/'AXI_Repository_Inventory_Register_v1.0.csv',
        log_file=phase1/'Logs'/'inventory_engine.log'
    )

if __name__=='__main__':
    cfg=load_config()
    print('Repository Root :',cfg.repository_root)
    print('Phase 1         :',cfg.phase1_root)
    print('Register XLSX   :',cfg.inventory_workbook)
