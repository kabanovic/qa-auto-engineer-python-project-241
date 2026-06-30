install:
	uv sync

test:
	uv run pytest --cov=gendiff --cov-report=xml --cov-report=term

lint:
	uv run ruff check gendiff tests

lint-fix:
	uv run ruff check --fix gendiff tests