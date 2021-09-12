# GCP cheat sheet

# BigQueryに時系列データを取り込んでリアルタイム分析

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


## storage service

### cloud storage

- htmlファイルをおけば簡易的ウェブサーバのようにもなる
    - ACL (アクセス制御リスト) でファイル単位のアクセス制限可能
- バケット単位でストレージクラスを設定
    - ストレージクラスは変更可能
        - standard
        - nearline
        - coldline
        - archive
- 期間をトリガーにした操作なども可能
    - ストレージクラスの変更やオブジェクトの削除など
- bucket名にはドメイン名(`.`付き)を使えるが、ドメインに対する所有権の証明が必要
- 署名付きURL
    - ユーザ認証なしでアクセス可能
- 鍵を使った暗号化できるが、なくすとデータ取り出せなくなる場合も
- 差分管理ではない
- VMディレクトリとの同期
- マルチリージョンではリージョン選択をできないので、企業などの制約ある場合は使えない

## メモ

- cloud shell
    - 5G永続ストレージ
- ゾーンはまとめて落ちる範囲
- 耐障害性を高めるならマルチリージョン

### ネットワーク

- VPC networkはアドレス範囲なし (private address)
    - 全リージョンにまたがる
- 1PJ以下に最大5つのVPCネットワーク定義可能
- VPCネットワーク内にはサブネットワーク定義可能
    - サブネットワークはリージョンを跨げない
- FWはVPCネットワーク単位
    - 同じVPC内のインスタンス同士でもFWを通過する
- VMの名前解決は同一VPCネットワーク内のみ可能
- VM内で`ifconfig`で確認できるのは内部IPのみ
    - 外部IPはメタデータから確認する
- cloudDNS -> googleのDNSサービス
- VMにはprimary以外のIPを設定可能
    - エイリアスIP範囲を使うとコンテナごとにIPを設定可能
- サブネットにも複数のアドレス範囲を割り振れる

### cloud sql

cloud sqlのインスタンスは次プロジェクト内ではなく、
サービス提供ベンダーのプロジェクト内に追加される


### GCP gaibu adress get
curl -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip && echo

## firewallのアドレス取得

```sh
cloud compute firewall-rules describe allow-ssh | \
        sed "/^sourceRanges:/,/^\[^-\s\].*/ ! d; {/^-/ ! d; s/^-\s\+//; s/$/,/}" | \
        sed -z "s/\n//g; s/,$//" | \
        xargs -i echo "{},`dig +short myip.opendns.com @resolver1.opendns.com`/32" | \
        xargs -i gcloud compute firewall-rules update allow-ssh --source-ranges={}
```

## AutoML

<https://cloud.google.com/automl>

- vertex API
    - <https://cloud.google.com/vertex-ai/docs>
- AutoML Vision
    - <https://cloud.google.com/vision/overview/docs#automl-vision>
- AutoML Video Intelligence (beta)
    - <https://cloud.google.com/video-intelligence/automl/docs>
    - AutoML Video Intelligence Classification
    - AutoML Video Intelligence Object Tracking
- AutoML Tables
    - <https://cloud.google.com/automl-tables/docs>
    - online analysis
        - <https://cloud.google.com/automl-tables/docs/predict>
