# Flask cheatsheet

## 使い方

- チュートリアルに基本的な構成方法の記述あり
  - <https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/tutorial/index.html>

### `__init__.py`を定義

- <https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/>

```
app/
  └ __init__.py
```

- `__init__.py`に`app`を作るfactory methodを定義
  - つまり設定等は`__init__.py`に書く

- `app/`と同じディレクトリで

```sh
export FLASK_APP=app
flask run
```

- `app/`内で

```sh
export FLASK_APP=.
flask run
```

## werkzeug warning

flaskはwerkzeugというサーバを内蔵しているが、プロダクションでの使用は推奨されない。

- <https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/>
> When running publicly rather than in development, you should not use the built-in development server (flask run). The development server is provided by Werkzeug for convenience, but is not designed to be particularly efficient, stable, or secure.

- <https://werkzeug.palletsprojects.com/en/2.0.x/serving/>
> The development server is not intended to be used on production systems. It was designed especially for development purposes and performs poorly under high load.

- <https://werkzeug.palletsprojects.com/en/2.0.x/middleware/http_proxy/>
> This middleware can only proxy HTTP requests, as HTTP is the only protocol handled by the WSGI server. Other protocols, such as WebSocket requests, cannot be proxied at this layer. This should only be used for development, in production a real proxy server should be used.

- <https://werkzeug.palletsprojects.com/en/2.0.x/deployment/>
  - デプロイの仕方について
