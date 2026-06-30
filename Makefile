install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check gendiff tests

lint-fix:
	uv run ruff check --fix gendiff tests