UV := uv
APP_NAME ?= gateway
SRC_DIR := services/$(APP_NAME)/app/run

run:
	cd services/$(APP_NAME) && $(UV) run python app/run

run-docker:
	cd services/$(APP_NAME) && docker compose up -d

run-all:
	@for service in $$(ls services); do \
		echo "🚀 Starting $$service..."; \
		cd services/$$service && \
		($(UV) run python app/run &) && \
		cd ../..; \
	done
	@echo "✅ All services started"

watch:
	$(UV) run watchmedo auto-restart \
			--directory=./services/$(APP_NAME) \
			--pattern="*.py" \
			--recursive \
			--verbose \
			-- $(UV) run python services/$(APP_NAME)/app/run

install:
	$(UV) sync --all-packages

lint:
	$(UV) run ruff check .

format:
	$(UV) run ruff check . --fix
	$(UV) run ruff format .

clean:
	rm -rf __pycache__ .pytest_cache .ruff_cache .coverage dist build *.egg-info
