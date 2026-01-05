# github-production-lab-python

A tiny "production workflow" lab repo to practice:
- feature branches
- pull requests (PRs)
- reviews + branch protection
- Python tooling (ruff, pytest)

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
pytest
ruff check .
```
