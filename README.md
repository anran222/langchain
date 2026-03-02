# langchain-app

A standard, mainstream Python project scaffold using the `src/` layout.

## Requirements

- Python 3.10+

## Quick Start

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Run

```bash
python -m langchain_app
# or
langchain-app
```

## Test and Lint

```bash
pytest
ruff check .
```

## Project Structure

```text
.
├─ .github/workflows/ci.yml
├─ docs/
├─ src/
│  └─ langchain_app/
│     ├─ __init__.py
│     ├─ __main__.py
│     └─ cli.py
├─ tests/
│  └─ unit/
│     └─ test_cli.py
├─ .editorconfig
├─ .gitignore
├─ LICENSE
├─ pyproject.toml
└─ README.md
```
