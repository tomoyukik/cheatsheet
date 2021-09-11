# 時系列DB

- <https://zenn.dev/nakabonne/articles/d300838a1500c7>
    - 時系列データベースを実装した記事
- <https://fukabori.fm/episode/53>
    - 時系列DBに関するラジオ
- write amplification
- gorilla
    - データ圧縮
    - <https://hnakamur.github.io/blog/2017/02/12/tried-facebook-gorilla-time-series-database-compression/>
    - <http://www.vldb.org/pvldb/vol8/p1816-teller.pdf>
    - タイムスタンプと値を分けてエンコーディング
        - 前後の値の関係性に焦点をあてて圧縮
        - 値はXOR/タイムスタンプは差分(delta encoding)
        - 値はfloat -> 実際の値は小さいビット数で表せる　-> XORとの相性がいい
    - <https://hnakamur.github.io/blog/2017/02/12/tried-facebook-gorilla-time-series-database-compression/>

## 時系列DB

- <https://www.sraoss.co.jp/wp-content/uploads/files/event_seminar/material/2020/dbts068_session_RDB.pdf>
    - 時系列DBとRDBの比較 (influxdb)
- <https://aws.amazon.com/jp/timestream/>
    - Amazon Timestream
    - amazonの時系列DB

## Datastream, CDC (Change DB Capture)
    - <https://cloud.google.com/blog/ja/products/data-analytics/how-to-move-data-from-mysql-to-bigquery>
        - MySQLからBigQuery
    - <https://cloud.google.com/blog/ja/products/databases/new-cloud-based-cdc-replication-across-databases>
        - Datastreamの活用
    - postgresには非対応
    - data streaming
        - <https://cloud.google.com/datastream>


## BigQuery streaming insert

- ストリーミングインサートで重複レコードを削除しながら BigQuery にデータをロードしてみた
    - <https://dev.classmethod.jp/articles/bigquery-streaming-insert-load-diff/>
- BigQueryへのデータのストリーミング
    - <https://cloud.google.com/bigquery/streaming-data-into-bigquery?hl=ja>

## センサーデータとDB

- リレーショナルではなく、生データを使用した方がパフォーマンスがいい
    - <https://blog.tinkermode.jp/entry/2019/12/09/181208>
- TimescaledDBというのがあるらしい
    - <https://www.infoq.com/jp/news/2019/07/timescale-multi-cloud/>
    - InfluxDB
        - <https://active.nikkeibp.co.jp/atcl/act/19/00005/022500414/>
- GCPでの時系列分析アーキテクチャ
    - <https://cloud.google.com/architecture/time-series-analysis?hl=ja>

