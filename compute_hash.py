#!/usr/bin/env python3
import hashlib, sys, pathlib

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: compute_hash.py <archivo_a_firmar>")
        sys.exit(1)
    p = pathlib.Path(sys.argv[1])
    digest = sha256_of_file(p)
    print(digest)