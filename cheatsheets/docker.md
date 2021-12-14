#docker #cheatsheet 
# Docker cheat sheet

## volume先のパス指定

volume先のディレクトリは絶対パスでないとうまくいかなかった。

```yaml
services:
  service1:
    volumes:
      - type: volume
        source: modules
        target: /usr/local/lib/python3.7/site-packages

volumes:
  modules:
    driver_opts:
      type: none
      device: /path/to/direcotry
      o: bind

```

## windowsでのdocker

- wsl2使わない場合、インストール時点で有効化しない様に気をつける
  - 有効かした場合は、docker desktopの設定から無効化できる
- 権限が制限されてるときは、管理者権限でdockerusersグループに操作ユーザを追加しないと使えない
- volumeを使うときはdocker desktopの設定から共有するディレクトリを設定しないとエラーが出る

## docker-composeのvolumeの書き方

- <https://zenn.dev/sarisia/articles/0c1db052d09921>

long syntax

```yaml
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

```sh
docker rm (docker ps -a -q)
```

## Dockerfileの配置

```console
root/
├ .dockerignore
└ docker/
  ├ Dockerfile
  └ docker-compose.yaml
```

上記構成でdocker-composeでbuild contextに`..`を指定すれば、
ビルドコンテキストルートは`root`になるので`.dockerignore`が適用される。
`Dockerfile`の中で`COPY . /app`とすれば、`.`は`root`の意味になる。

## workdir

- `WORKDIR`はディレクトリも作成する
    - <http://docs.docker.jp/engine/reference/builder.html#workdir>

## 証明書に関して

- <https://docs.docker.com/engine/security/certificates/>

dockerでは、dockerでのみ使用したい証明書を`/etc/docker/certs.d/`以下のレジストリのホスト名と同名のディレクトリを作成し、配置することで使用できる。
linuxでは任意のCAはシステムデフォルトとマージされる。
windowsでは、システムデフォルトの証明書はカスタムルートCAが設定されていない場合のみ使用される。

つまり、Linuxの場合、OSと共通で使用したい証明書はOSの設定で問題なく、
dockerのみで使用したいイメージがあった場合はカスタムが必要になる、と理解した
レジストリからのイメージのpullを前提に話をしているが、docker image以外のパッケージとかをイメージ中でインストールしたい場合の証明書も同じなんだろうか。

- <https://knqyf263.hatenablog.com/entry/2019/11/29/052818>
    - `curl`でdocker pullできるみたいだからcurlではできるのにdocker pullではできないみたいに検証に使えそう

- <https://taktak.jp/2019/11/30/4211/>

## build環境依存の変数は`--build-arg`に定義する

- <https://docs.docker.jp/engine/reference/commandline/build.html#build-arg>
