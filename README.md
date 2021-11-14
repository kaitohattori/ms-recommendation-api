# MS Recommendation API

## 準備

```
$ pyenv version   
3.7.2 (set by /Users/kaito/.pyenv/version)

$ pip install -r requirements.txt
```

## 動作

```
# 実行
$ python main.py
```

```
# 実行
$ make run

# Dockerビルド
$ make docker-build

# Docker実行
$ make docker-run

# Docker Compose系
$ make docker-compose-build
$ make docker-compose-up
$ make docker-compose-down
$ make docker-compose-run // build & up
```

## ドキュメント

http://localhost:8082/docs/api/v1/
