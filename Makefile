NAME = ms-recommendation-api
POSTGRESQL = postgresql

run: ## Run on local
	python main.py

docker-build: ## Build on docker
	docker build -t $(NAME) .

docker-run: ## Run on docker
	docker run --name $(NAME) --rm -p 8082:8082 $(NAME)

external-run:
	docker run -d \
		-p 5432:5432 \
		-e POSTGRES_DB=video \
		-e POSTGRES_USER=root \
		-e POSTGRES_PASSWORD=root \
		-e POSTGRES_INITDB_ARGS="--encoding=UTF-8" \
		-v $(PWD)/db/:/docker-entrypoint-initdb.d \
		--name $(POSTGRESQL) \
		postgres:latest

external-end:
	docker stop $(POSTGRESQL)
	docker rm $(POSTGRESQL)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
