install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

local-games:
	uv run brain-games --link-mode=copy

build:
	uv build

package-install:
	uv tool install dist/*.whl

install-force:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games
