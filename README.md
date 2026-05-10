1. To start app locally:
```bash
uv run uvicorn src.app:app --reload
```

or

```bash
uv run litestar --app-dir src --app app:app run --reload
```


export LITESTAR_APP=main:app

uv run litestar --app-dir src --app app:app database
1. make-migrations
2. upgrade

ruff checks:
uv run ruff check
uv run ruff check --fix
uv run ruff format
