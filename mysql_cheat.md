# mysql cheat sheet

## Dockerでのmysql環境の構築方法

```
mysql:
    image: mysql:8
    environment:
        MYSQL_ROOT_PASSWORD: password
        MYSQL_DATABASE: mydatabase
        MYSQL_USER: user
        MYSQL_PASSWORD: password
    ports:
        - 3306:3306
    volumes:
        - ./mysql:/var/lib/mysql
        - ./my.cnf:/etc/mysql/my.cnf
```

```
[mysqld]
secure-file-priv=/path/to/directory
```

```
docker-compose exec mysql bash -c 'mysql mydatabase < /path/to/sql/file.sql'
```

## tsvのインポート方法

```
LOAD DATA INFILE 'path/to/tsv/file.tsv' INTO TABLE mytable
    FILEDS TERMINAED BY '\t'
    IGNORE 1 LINES
    (@id, @surname, @lastname)
    id = NULLIF(@id, ''),
    surname = @surname,
    lastname = @lastname
;
```

- `(@id, @surname, @lastname)`でインポートするファイルの各カラムに変数名をセット
- `id = NULLIF(@id, '')` はdbの`id`カラムに対して、ファイルの`@id`カラムをインポートするとき空文字なら`NULL`にするという指定
- 多分@で変数設定する場合、SET句で代入する必要がある
