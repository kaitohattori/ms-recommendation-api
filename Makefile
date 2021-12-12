APP_NAME = ms-recommendation-api
POSTGRESQL = postgresql

run: ## Run on local
	python main.py

docker-build: ## Build on docker
	docker build -t $(APP_NAME) .

docker-run: ## Run on docker
	docker run --name $(APP_NAME) --rm -p 8082:8082 $(APP_NAME)

external-run: ## Run external apps
	docker run -d \
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
	docker rm $(POSTGRESQL)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
