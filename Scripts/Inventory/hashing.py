"""
AXI Inventory Engine - File Hashing
Module: hashing.py
Project: AXI-ENG-001
Version: 1.0.0
"""

from __future__ import annotations

import hashlib
from pathlib import Path

DEFAULT_CHUNK_SIZE = 1024 * 1024  # 1 MB


def sha256_file(file_path: Path, chunk_size: int = DEFAULT_CHUNK_SIZE) -> str:
    """Return the SHA-256 checksum for a file."""
    hasher = hashlib.sha256()

    with file_path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()


def verify_checksum(file_path: Path, expected: str) -> bool:
    """Verify a file against an expected SHA-256 checksum."""
    return sha256_file(file_path).lower() == expected.lower()


if __name__ == "__main__":
    target = Path(__file__)
    checksum = sha256_file(target)

    print("=" * 50)
    print("AXI Hashing Module v1.0")
    print("=" * 50)
    print(f"File     : {target.name}")
    print(f"SHA-256  : {checksum}")
    print(f"Verified : {verify_checksum(target, checksum)}")
