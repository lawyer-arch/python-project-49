setup: install build package-install

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

.PHONY: install brain-games build package-install
