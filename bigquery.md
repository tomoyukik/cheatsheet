# BigQuery Cheat Sheet

## クエリ結果書き込み

クエリ結果をcsvダウンロードするにはコンソールが必要

<https://cloud.google.com/bigquery/docs/writing-results?hl=ja>

## console操作

```sh
> bq ls dataset名
> bq query "SELECT column FROM table"
```

## Pythonでbigquery

### ライブラリインストール

BigQuery client library ver. 1.9.0以降

```sh
pip install --upgrade google-cloud-bigquery[bgstorage, pandas]
```

### 基本的な使い方

```python
# 環境変数に設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/credential.json'
client = bigquery.Client(project='priject_id')

df = client.query('SQL', location='asia-northeast').to_dataframe()
```

### マジックコマンド

```python
import google.cloud.bigquery.magics
google.cloud.bigquery.magics.context.use_bgstorage_api = Ture

%% bigquery --project プロジェクトID　df_temp
SELECT columns FROM table
```

### google cloud storage api

```python
from google.cloud import bigquery
from google.cloud import bigquery_storage_v1beta1

query = "SELECT column FROM table"

client = bigquery.Client(project='プロジェクトID')
storage_client = bigquery_storage_v1beta1.BigQueryStorageClient()
df_temp = client.query(query).to_dataframe(storage_client)
```

## BigQueryに時系列データを取り込んでリアルタイム分析

- パーティショニングテーブルを用いることでコスト削減ができる
    - <https://cloud.google.com/bigquery/docs/querying-partitioned-tables?hl=ja>
- リアルタイム分析にはBigTableも使えるが、高額になりがち
    - 本当に速度を求める場合に使うのがいい
    - BigTableはNoSQL
- 時間単位列パーティション
    - TIMESTAMP 列と DATETIME 列では、パーティションを時間単位、日単位、月単位、年単位
    - 月単位、年単位のいずれで作成できます。
    - パーティションの境界は UTC 時間
    - 列の値に基づいて、自動的に正しいパーティションにデータを入力
    - 取り込み時間パーティショニングというのもある
        - 列値ではなく取り込んだ時間をもとにパーティショニング
    - パーティショニングには上限あり (4000)
        - <https://cloud.google.com/bigquery/quotas#partitioned_tables>
        - 超える場合はクラスタリング採用
        - 時間別で分けると 12 x 365 > 4000 なので、1年以内にクラスタリングが必要
        - 日別で分けると 365 x 10 < 4000 なので10年以上はクラスタリング不要
- シャーディング
    - 接頭辞を使ってテーブル分割する仕組み
    - <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_clustering>
- sandboxで試用ができる？
    - <https://cloud.google.com/bigquery/docs/sandbox?hl=ja>
- sensor data collection and analytics
    - <https://cloud.google.com/community/tutorials/cloud-iot-enviro-board-workshop>
- IoT Core との組み合わせ
    - <https://cloud.google.com/iot-core>
- Fluentdとの組み合わせ
    - <https://cloud.google.com/architecture/fluentd-bigquery?hl=ja>
- bigquery ml
    - <https://cloud.google.com/bigquery-ml/docs/introduction?hl=ja>
    - automl model
        - <https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-automl?hl=ja>
