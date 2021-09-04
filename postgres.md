# postgres cheat sheet

## `JSON_AGG`

`GROUP BY`したときに、aggするカラムの重複を無くしたい。

```json
[
    id: 1, values: [{id: 1, name: 'UK'}, {id: 1, name: 'US'}],
    id: 2, values: [{id: 2, name: 'japan'}],
]
```

みたいになるのを

```json
[
    id: 1, values: [{name: 'UK'}, {name: 'US'}],
    id: 2, values: [{name: 'japan'}],
]
```

にしたい。

- <https://dba.stackexchange.com/questions/69655/select-columns-inside-json-agg>

1. サブクエリ
    ```sql
    SELECT a.id, a.name
        , JSON_AGG((
            SELECT x FROM (SELECT b.col1, b.col2, b.col3) AS x
        )) AS item
    FROM   a
    JOIN   b ON b.item_id = a.id
    GROUP  BY a.id, a.name;
    ```
2. `JSON_BUILD_OBJECT`
    ```sql
    SELECT a.id, a.name
        , JSON_AGG(
            JSON_BUILD_OBJECT('col1', b.col1, 'col2', b.col2, 'col3', b.col3)
        ) AS item
    FROM   a
    JOIN   b ON b.item_id = a.id
    GROUP  BY a.id, a.name;
    ```

個人的好みは1だけど、ここまでsqlで頑張りたくない。
