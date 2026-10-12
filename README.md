# ENPM605 Spring 2027: course code

Set up once, from the root of this repository:

```bash
uv venv --python /usr/bin/python3 --system-site-packages
uv sync
uv run lecture1/verify_setup.py
```

Create the virtual environment with `uv venv` **before** the first
`uv sync`. The `--system-site-packages` flag lets the environment see
Ubuntu's packages, which ROS 2 needs from Lecture 8.
