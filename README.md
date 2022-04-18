# MS Recommendation API

## Prerequisites

```
$ pyenv version   
3.7.2 (set by /Users/kaito/.pyenv/version)

# Initialize app
$ make init
```

Set setting file at `settings/settings.ini`

## How to develop

```
# Run on local
$ make run

# Build on docker
$ make docker-build

# Run on docker
$ make docker-run

# Run external apps
$ make external-up

# End external apps
$ make external-down

# Help
$ make help
```

## API Docs

http://localhost:8082/docs/api/v1/

## Deploy

Deploy to minikube

```
# Start minikube
$ minikube start

# Use local image
$ eval $(minikube docker-env)

# Build docker image
$ docker build -t ms-recommendation-api .

# Deploy
$ kubectl apply -f deploy/configmap.yaml
$ kubectl apply -f deploy/deployment.yaml
$ kubectl apply -f deploy/service.yaml

# Get all status
$ kubectl get all | grep "ms-recommendation-api"

# Access to deployed app (Click the displayed url)
$ minikube service ms-recommendation-api --url
```

minikube common commands

```
$ minikube start
$ minikube status
$ minikube dashboard
$ minikube tunnel
$ minikube stop
```
