install:
	uv sync

brain-games:
	uv run brain-games

local-games:
	uv run brain-games --link-mode=copy

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games
