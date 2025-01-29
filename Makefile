setup: install

install:
	uv sync

brain-games:
	uv run brain-games

.PHONY: install brain-games
