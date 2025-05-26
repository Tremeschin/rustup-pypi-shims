import os
import shutil
import sys
from pathlib import Path


# Todo: Get from venv directly
def path() -> Path:
    return Path(shutil.which("rustup"))

# Note: This function replaces the current process on unix
#   and spawns a new one on Windows, there's no going back
#   to the current Python interpreter process!
def _shim(proxy: str) -> None:
    os.execv(path(), (proxy, *sys.argv[1:]))

def init() -> None:
    _shim("rustup-init")

def cargo() -> None:
    _shim("cargo")

def cargo_clippy() -> None:
    _shim("cargo-clippy")

def cargo_fmt() -> None:
    _shim("cargo-fmt")

def cargo_miri() -> None:
    _shim("cargo-miri")

def clippy_driver() -> None:
    _shim("clippy-driver")

def rls() -> None:
    _shim("rls")

def rust_analyzer() -> None:
    _shim("rust-analyzer")

def rust_gdb() -> None:
    _shim("rust-gdb")

def rust_gdbgui() -> None:
    _shim("rust-gdbgui")

def rust_lldb() -> None:
    _shim("rust-lldb")

def rustc() -> None:
    _shim("rustc")

def rustdoc() -> None:
    _shim("rustdoc")

def rustfmt() -> None:
    _shim("rustfmt")
