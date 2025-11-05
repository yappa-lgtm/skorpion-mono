UV := uv
APP_NAME ?= gateway
SRC_DIR := services/$(APP_NAME)/app/run

run:
	cd services/$(APP_NAME) && $(UV) run python app/run

install:
	$(UV) sync --all-packages

lint:
	$(UV) run ruff check .

format:
	$(UV) run ruff check . --fix
	$(UV) run ruff format .

clean:
	rm -rf __pycache__ .pytest_cache .ruff_cache .coverage dist build *.egg-info
