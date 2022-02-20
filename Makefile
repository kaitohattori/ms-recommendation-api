APP_NAME = ms-recommendation-api
EXTERNAL_APPS = postgresql

init: ## Initialize app
	pip install -r requirements.txt

run: ## Run on local
	python main.py

docker-build: ## Build on docker
	docker build -t $(APP_NAME) .

docker-run: ## Run on docker
	docker run --rm \
		-p 8082:8082 \
		-v ./logs:/app/logs \
		--name $(APP_NAME) \
		$(APP_NAME):latest

external-init: ## Initialize external apps
	rm -rf ./external-apps/assets
	rm -rf ./external-apps/logs

external-run: ## Run external apps
	docker-compose up -d $(EXTERNAL_APPS)

external-end: ## End external apps
	docker-compose down

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
