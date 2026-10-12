import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lecture1"))

from verify_setup import (
    check_numpy,
    check_python,
    check_ruff,
    check_system_site,
    check_venv,
)


def test_python_312_passes():
    assert check_python((3, 12))[0]


def test_other_python_fails():
    ok, message = check_python((3, 14))
    assert not ok
    assert "3.14" in message


def test_venv_detected():
    assert check_venv("/home/u/enpm605/.venv", "/usr")[0]


def test_no_venv_fails():
    assert not check_venv("/usr", "/usr")[0]


def test_system_site_true_passes():
    cfg = "home = /usr/bin\ninclude-system-site-packages = true\n"
    assert check_system_site(cfg)[0]


def test_system_site_false_fails_and_says_how_to_fix():
    ok, message = check_system_site("include-system-site-packages = false\n")
    assert not ok
    assert "--system-site-packages" in message


def test_system_site_fix_replaces_the_existing_venv():
    # "uv venv" refuses to run over an existing .venv; the fix must say --clear
    _, message = check_system_site("include-system-site-packages = false\n")
    assert "uv venv --clear --python /usr/bin/python3 --system-site-packages" in message
    assert "uv sync" in message


def test_missing_pyvenv_cfg_fails():
    assert not check_system_site(None)[0]


def test_numpy_1_passes():
    assert check_numpy("1.26.4")[0]


def test_numpy_2_fails():
    assert not check_numpy("2.5.4")[0]


def test_numpy_missing_fails():
    assert not check_numpy(None)[0]


def test_ruff_found_and_missing():
    assert check_ruff("/x/.venv/bin/ruff")[0]
    assert not check_ruff(None)[0]
