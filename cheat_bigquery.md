# BigQuery Cheat Sheet

## クエリ結果書き込み

クエリ結果をcsvダウンロードするにはコンソールが必要

https://cloud.google.com/bigquery/docs/writing-results?hl=ja

## Pythonでbigquery

```python
# 環境変数に設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/credential.json'
client = bigquery.Client(project='priject_id')

df = client.query('SQL', location='asia-northeast').to_dataframe()
```
