PY ?= python3

.PHONY: test lint deck models clean

test:
	$(PY) -m pytest tests/ -o addopts=""

lint:
