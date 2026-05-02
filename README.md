1. To start app locally:
```bash
uv run uvicorn src.app:app --reload
```


export LITESTAR_APP=main:app

uv run litestar --app-dir src --app app:app database 

ruff checks:
uv run ruff check
uv run ruff check --fix
uv run ruff format
