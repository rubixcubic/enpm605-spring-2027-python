"""Check the ENPM605 Python environment (Lecture 1).

Run from the root of the course repository:

    uv run lecture1/verify_setup.py

Each check prints [ OK ] or [FAIL]. The program exits with 0 when every
check passes and with 1 otherwise.
"""

import importlib.metadata
import shutil
import sys
from pathlib import Path

REQUIRED_PYTHON = (3, 12)
RECREATE_VENV = (
    "'uv venv --clear --python /usr/bin/python3 --system-site-packages', then 'uv sync'"
)


def check_python(version: tuple[int, int]) -> tuple[bool, str]:
    """Pass when the interpreter is Python 3.12, the version ROS 2 Jazzy uses."""
    found = f"{version[0]}.{version[1]}"
    return version == REQUIRED_PYTHON, f"Python {found} (need 3.12)"


def check_venv(prefix: str, base_prefix: str) -> tuple[bool, str]:
    """Pass when Python runs inside a virtual environment."""
    if prefix != base_prefix:
        return True, f"virtual environment at {prefix}"
    return False, "not inside a virtual environment"


def check_system_site(pyvenv_cfg: str | None) -> tuple[bool, str]:
    """Pass when the venv can see Ubuntu's packages (ROS 2 needs them from Lecture 8)."""
    if pyvenv_cfg is None:
        return False, "no pyvenv.cfg: not a virtual environment"
    if "include-system-site-packages = true" in pyvenv_cfg:
        return True, "system site packages visible"
    return False, f"system site packages hidden: run {RECREATE_VENV}"


def check_numpy(version: str | None) -> tuple[bool, str]:
    """Pass when NumPy is installed and below 2 (ROS 2 Jazzy is built against NumPy 1)."""
    if version is None:
        return False, "NumPy not installed"
    major = int(version.split(".")[0])
    return major < 2, f"NumPy {version} (need below 2)"


def check_ruff(path: str | None) -> tuple[bool, str]:
    """Pass when the ruff command is on the PATH."""
    if path is None:
        return False, "Ruff not found"
    return True, f"Ruff at {path}"


def numpy_version() -> str | None:
    try:
        return importlib.metadata.version("numpy")
    except importlib.metadata.PackageNotFoundError:
        return None


def read_pyvenv_cfg(prefix: str) -> str | None:
    cfg = Path(prefix) / "pyvenv.cfg"
    return cfg.read_text() if cfg.exists() else None


def main() -> int:
    results = [
        check_python(sys.version_info[:2]),
        check_venv(sys.prefix, sys.base_prefix),
        check_system_site(read_pyvenv_cfg(sys.prefix)),
        check_numpy(numpy_version()),
        check_ruff(shutil.which("ruff")),
    ]
    for ok, message in results:
        print(f"[{' OK ' if ok else 'FAIL'}] {message}")
    passed = sum(ok for ok, _ in results)
    print(f"{passed} of {len(results)} checks passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
