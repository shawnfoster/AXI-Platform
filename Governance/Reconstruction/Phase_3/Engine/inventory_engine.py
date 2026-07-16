from pathlib import Path
import sys
from config import load_config
from scanner import scan_repository
from writers import write_outputs
def main():
    if len(sys.argv)<2:
        print('Usage: python inventory_engine.py <repo>');return 1
    root=Path(sys.argv[1]).resolve()
    cfg=load_config(root)
    rows=scan_repository(root)
    write_outputs(rows,cfg.inventory_dir)
    print(f'Inventoried {len(rows)} artifacts.')
if __name__=='__main__':
    raise SystemExit(main())
