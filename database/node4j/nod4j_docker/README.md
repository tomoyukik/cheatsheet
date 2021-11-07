# neo4j docker環境

```
docker compose up
```

`localhost:7474`でブラウザからアクセス

デフォルトのユーザ名とパスワードはneo4j

## cypher-shellの利用

- https://neo4j.com/developer/docker-run-neo4j/

```
docker compose exec db cypher-shell -u user -p password
```

`:exit`で抜ける。

## SQLファイル実行

```
docker compose exec db bash
cypher-shell -u user -p passowrd < file.sql
```

