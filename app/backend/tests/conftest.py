"""Shared pytest fixtures for DynaChat backend tests.

Conventions (see CLAUDE.md §Testing):
- Use pytest-asyncio for async tests (`@pytest.mark.asyncio` or the
  `asyncio_mode = "auto"` mode configured in `pyproject.toml`).
- Use `httpx.AsyncClient` against a test FastAPI app for integration tests.
- Tests must NEVER touch `app/backend/data/chat.db`. Spin up a temp SQLite
  database per-test via the `tmp_path` fixture.
"""
