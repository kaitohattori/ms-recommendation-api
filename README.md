# MS Recommendation API

## 準備

```
$ pyenv version   
3.7.2 (set by /Users/kaito/.pyenv/version)

# APP初期設定
$ make init
```

`settings/settings.ini` を配置してください。

## 実行コマンド

```
# 実行
$ make run

# Dockerビルド
$ make docker-build

# Docker実行
$ make docker-run

# external appsを立ち上げる
$ make external-run

# external appsを終了する
$ make external-end

# ヘルプ
$ make help
```

## ドキュメント

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
