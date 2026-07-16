import hashlib
def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for c in iter(lambda:f.read(1048576),b''):
            h.update(c)
    return h.hexdigest()
