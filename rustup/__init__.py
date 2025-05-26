import os
import shutil
import sys
from pathlib import Path


# Todo: Get from venv directly
def path() -> Path:
    return Path(shutil.which("rustup"))

def _make_shim(proxy: str, args: list[str]=None) -> None:
    if args is None:
        args = sys.argv[1:]
    os.execv(path(), (proxy, *args))

def init(args: list[str]=None) -> None:
    _make_shim("rustup-init", args)

def cargo(args: list[str]=None) -> None:
    _make_shim("cargo", args)

def rustc(args: list[str]=None) -> None:
    _make_shim("rustc",*args)
