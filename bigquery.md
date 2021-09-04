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

