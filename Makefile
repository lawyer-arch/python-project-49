setup: install build package-install

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --reinstall  dist/*.whl

make lint:
	uv run ruff check brain_games

.PHONY: install brain-games build package-install lint
