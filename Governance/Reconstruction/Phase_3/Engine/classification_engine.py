
from pathlib import Path
import json,csv

CLASS_MAP={
    ".py":"Script",".md":"Documentation",".txt":"Notes",".csv":"Dataset",
    ".xlsx":"Spreadsheet",".docx":"Document",".pdf":"Report",
    ".pptx":"Presentation",".png":"Image",".jpg":"Image",".jpeg":"Image",
    ".svg":"Image",".yaml":"Configuration",".yml":"Configuration",".json":"Data"
}

def classify(rec):
    ext=Path(rec["filename"]).suffix.lower()
    c=CLASS_MAP.get(ext,"Review")
    rec2=dict(rec)
    rec2["classification"]=c
    rec2["category"]="Governance" if "Governance" in rec["relative_path"] else "General"
    rec2["lifecycle"]="Archive" if "Archive/" in rec["relative_path"] else "Active"
    rec2["confidence"]=1.0 if c!="Review" else 0.25
    rec2["review_required"]= c=="Review"
    rec2["classification_rule"]=f"extension:{ext or '<none>'}"
    return rec2

def main():
    root=Path(".").resolve()
    inv=root/"Governance/Reconstruction/Phase_3/Inventory/AXI-REG-001_Artifact_Inventory.json"
    outdir=root/"Governance/Reconstruction/Phase_3/Classification"
    outdir.mkdir(parents=True,exist_ok=True)
    data=json.loads(inv.read_text())
    rows=[classify(r) for r in data]
    with open(outdir/"AXI-REG-003_Artifact_Classification.json","w") as f:
        json.dump(rows,f,indent=2)
    with open(outdir/"AXI-REG-003_Artifact_Classification.csv","w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    summary={
      "classified":len(rows),
      "review_required":sum(1 for r in rows if r["review_required"])
    }
    (outdir/"classification_summary.json").write_text(json.dumps(summary,indent=2))
    (outdir/"classification_log.txt").write_text("Completed\n")
    print(f"Classified {len(rows)} artifacts.")
if __name__=="__main__":
    main()
