# MS Recommendation API

## 準備

```
$ pyenv version   
3.7.2 (set by /Users/kaito/.pyenv/version)

# APP初期設定
$ make init
```

`settings.ini` を settings/以下に配置してください。

## 動作

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
