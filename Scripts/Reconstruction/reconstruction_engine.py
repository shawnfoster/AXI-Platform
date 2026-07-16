#!/usr/bin/env python3

from pathlib import Path
import runpy
import sys

target = (
    Path(__file__).resolve().parents[2]
    / "Engines"
    / "Reconstruction"
    / "reconstruction_engine.py"
)

runpy.run_path(str(target), run_name="__main__")
