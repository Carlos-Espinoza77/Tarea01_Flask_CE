# AGENTS.md

## Project

Simple Flask web app — university assignment ("Tarea 01").

## Stack

- **Python 3.14** (`.python-version`)
- **Flask 3.1.3+** (`pyproject.toml`)
- **uv** package manager (`uv.lock`)

## Commands

| Action | Command |
|---|---|---|
| Install deps | `uv sync` |
| Run dev server | `uv run python main.py` |
| Add dependency | `uv add <package>` |

The app runs in debug mode by default (`main.py:10`).

## Structure

- `main.py` — single entrypoint (Flask app)
- `templates/index.html` — the only template (Jinja2)
- `LabJupyter.ipynb` — companion notebook (pandas, exploration)

## Notes

- No tests, no CI, no linter/formatter config, no database.
- The `.venv` is pre-created and tracked in `.gitignore`.
- `templates/index.html` exists but is **not** currently rendered by the route — `main.py:7` returns a raw string.
