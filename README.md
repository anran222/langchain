# langchain-app

一个可直接开发、测试与打包的 Python 项目模板。

## 环境要求

- Python 3.10+

## 快速开始

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## 运行

```bash
python main.py
# 或
langchain-app
```

## 测试与检查

```bash
pytest
ruff check .
```

## 项目结构

```text
.
├─ src/
│  └─ langchain_app/
│     ├─ __init__.py
│     └─ cli.py
├─ tests/
│  └─ test_cli.py
├─ main.py
└─ pyproject.toml
```
