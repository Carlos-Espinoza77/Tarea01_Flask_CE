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

The app runs in debug mode by default (`app/__init__.py` calls `app.run(debug=True)` via `main.py`).

## Structure

- `main.py` — entrypoint (creates app via factory)
- `app/__init__.py` — Flask app factory (`create_app()`)
- `app/config.py` — config class (reads `SECRET_KEY` from env)
- `app/routes/` — blueprints (currently `main_bp` at `/`)
- `app/templates/` — Jinja2 templates
- `app/static/` — static files
- `app/utils/` — utility modules
- `app/database/` — database helpers (future)
- `LabJupyter.ipynb` — companion notebook (pandas, exploration)

## Notes

- No tests, no CI, no linter/formatter config, no database.
- The `.venv` is pre-created and tracked in `.gitignore`.
- All config comes from environment variables (loaded via `python-dotenv` from `.env`).
  `SECRET_KEY` **is required** — the app raises `RuntimeError` if unset.
- `FLASK_ENV` controls `ENV` / `DEBUG` (default `development`).
- `DATABASE_URL` defaults to `sqlite:///bdatos.db`.
