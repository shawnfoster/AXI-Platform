import csv,json
from pathlib import Path
def write_outputs(rows,outdir:Path):
    if not rows:return
    fields=list(rows[0].keys())
    with open(outdir/'AXI-REG-001_Artifact_Inventory.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    with open(outdir/'AXI-REG-001_Artifact_Inventory.json','w') as f:
        json.dump(rows,f,indent=2)
