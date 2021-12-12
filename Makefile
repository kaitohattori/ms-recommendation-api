APP_NAME = ms-recommendation-api
POSTGRESQL = postgresql
DOCKER_STORAGE_PATH = ~/ms-tv

run: ## Run on local
	python main.py

docker-build: ## Build on docker
	docker build -t $(APP_NAME) .

docker-run: ## Run on docker
	docker run --rm \
		-p 8082:8082 \
		-v $(DOCKER_STORAGE_PATH)/logs:/app/logs \
		--name $(APP_NAME) \
		$(APP_NAME):latest

external-run: ## Run external apps
	docker run -d --rm \
		-p 5432:5432 \
		-e POSTGRES_DB=video \
		-e POSTGRES_USER=root \
		-e POSTGRES_PASSWORD=root \
		-e POSTGRES_INITDB_ARGS="--encoding=UTF-8" \
		-v $(PWD)/db/:/docker-entrypoint-initdb.d \
		--name $(POSTGRESQL) \
		postgres:latest

external-end: ## End external apps
	docker stop $(POSTGRESQL)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
