from pathlib import Path
import os,mimetypes
from hashing import sha256
IGNORE={'.git','__pycache__','.venv','venv','node_modules'}
def scan_repository(root):
    rows=[];i=1
    for dp,dns,fns in os.walk(root):
        dns[:]=[d for d in dns if d not in IGNORE]
        for fn in fns:
            p=Path(dp)/fn
            st=p.stat()
            mime,_=mimetypes.guess_type(str(p))
            rows.append({'artifact_id':f'AXI-ART-{i:06d}','sha256':sha256(p),'filename':p.name,'relative_path':str(p.relative_to(root)),'size_bytes':st.st_size,'mime_type':mime or 'application/octet-stream'})
            i+=1
    return rows
