# Docker Cheat

## volumeするときにcontainerの中身をlocalにvolumeする方法

volumeを宣言するとき、ディレクトリじゃなくてvolumeで宣言する

```
    volumes:
      - conf:/etc/httpd/conf.d
```

localにvolumeと同名のディレクトリを作成する
```
mkdir conf
```

containerを起動すると中身ができてる

以下の宣言方法だと、ローカルのディレクトリでコンテナのディレクトリを上書きする
```
volumes:
  - ./conf:/etc/httpd/conf.d
```

## windowsでのdocker

- wsl2使わない場合、インストール時点で有効化しない様に気をつける
  - 有効かした場合は、docker desktopの設定から無効化できる
- 権限が制限されてるときは、管理者権限でdockerusersグループに操作ユーザを追加しないと使えない
- volumeを使うときはdocker desctopの設定から共有するディレクトリを設定しないとエラーが出る

## docker-composeのvolumeの書き方

- https://zenn.dev/sarisia/articles/0c1db052d09921

long syntax

```
    volumes:
      - type: bind
        source: "./config"
        target: "/config"
```

`./app.sock:/var/run/app.sock`(short syntax)で書くとディレクトリが作成されるけど、上記だとディレクトリがない場合にエラーが出る。
空ディレクトリをマウントしたいときはshort syntaxでいいかもしれない。

## `docker-compose`で`-it`オプション

```yaml
tty: true # -t
stdin_open: true # -i
```

## Dockerfile指定

```Dockerfile
build:
    context: .
    dockerfile: .
    image: image_name
    container_name: container_name
```

### fishでdocker container一括削除

```
docker rm (docker ps -a -q)
```
