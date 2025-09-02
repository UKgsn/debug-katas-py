# Debug Katas (Python)
A set of intentionally buggy Python functions with unit tests to demonstrate debugging, testing, and CI/CD.

## Features
- Python 3.11+
- Unit tests with pytest + Hypothesis
- Type checks with mypy
- Linting with ruff
- CI/CD via GitHub Actions

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
