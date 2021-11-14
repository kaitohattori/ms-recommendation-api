NAME = ms-recommendation-api

run: ## Run on local
	python main.py

docker-build: ## Build on docker
	docker build -t $(NAME) .

docker-run: ## Run on docker
	docker run --name $(NAME) --rm -p 8082:8082 $(NAME)

docker-compose-build: ## Build by docker-compose
	docker-compose build

docker-compose-up: ## docker-compose up
	docker-compose up

docker-compose-down: ## Stop by docker-compose
	docker-compose down

docker-compose-run: ## Run by docker-compose
	make docker-compose-build
	make docker-compose-up

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
