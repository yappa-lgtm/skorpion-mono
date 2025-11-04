UV := uv
APP_NAME ?= gateway
SRC_DIR := services/$(APP_NAME)/app/run

run:
	$(UV) run --package $(APP_NAME) python $(SRC_DIR)

install:
	$(UV) sync --all-packages

lint:
	$(UV) run ruff check .

format:
	$(UV) run ruff check . --fix
	$(UV) run ruff format .

clean:
	rm -rf __pycache__ .pytest_cache .ruff_cache .coverage dist build *.egg-info
