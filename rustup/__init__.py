import os
import shutil
import sys
from pathlib import Path


# Todo: Get from venv directly
def path() -> Path:
    return Path(shutil.which("rustup"))

def _make_shim(proxy: str) -> None:
    os.execv(path(), (proxy, *sys.argv[1:]))

def init() -> None:
    _make_shim("rustup-init")

def cargo() -> None:
    _make_shim("cargo")

def rustc() -> None:
    _make_shim("rustc")
