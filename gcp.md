# GCP cheat sheet

## BigQueryに時系列データを取り込んでリアルタイム分析

- パーティショニングテーブルを用いることでコスト削減ができる
    - https://cloud.google.com/bigquery/docs/querying-partitioned-tables?hl=ja
- リアルタイム分析にはBigTableも使えるが、高額になりがち
    - 本当に速度を求める場合に使うのがいい
    - BigTableはNoSQL

## コンテナ

- GKEの代わりにGAEが使えるのでは？
    - そうでもない？ -> 使えそう
    - そうでも無い意見
        - <https://www.mpon.me/entry/2018/05/02/133908>
- k8sで建てているコンテナは、APIがシンプルでRESTなどのAPIに制限されている場合はGAE、Cloud Ran、Cloud Functionも使える
    - マニフェストファイルが不要になるため、やや管理が楽になる
    - 定期実行など、トリガーでコンテナが起動できればいい場合は、Cloud RanかCloud Functionを検討すべき


## cloud build

- 置換変数
    - <https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values?hl=ja>
- GKEへのデプロイ
    - <https://cloud.google.com/build/docs/deploying-builds/deploy-gke?hl=ja#yaml_1>
    - <https://cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build?hl=ja>
        - マニフェストファイルの例あり

- gitops style
    - <https://cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build>
    - CDパイプラインの図とチュートリアル