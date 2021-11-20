# MS Recommendation API

## 準備

```
$ pyenv version   
3.7.2 (set by /Users/kaito/.pyenv/version)

$ pip install -r requirements.txt
```

`settings.ini` を settings/以下に配置してください。

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
```

## ドキュメント

http://localhost:8082/docs/api/v1/
