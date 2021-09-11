# マイクロサービス

### マイクロサービスの特徴

- 疎結合性
- 高凝縮性

疎結合性に気を取られすぎて高凝縮性を悪れがち

参照: <https://syobochim.hatenablog.com/entry/2020/05/01/083200>


## メモ

- マイクロサービスアーキテクチャ (MSA) ではサービスごとにDBを持たせて、複数のサービスから共有しないらしい。
    - [絵で見てわかるマイクロサービスの仕組み][1]
    - ビッグデータとかは？
    - ML関連だと分けるの難しくない？
    - DBの単位がサービスになる？
- サービスごとにDBが重複するらしい
    - [日経クロステック] [2] (無料会員時だから最後まで読めない)
    - 本当？

- [絵で見てわかるマイクロサービスの仕組み][1]
    - CNCF (Cloud Native Computing Foundation)
    - [Cloud Native Interactive Foundation][3]
    - コンウェイの法則
    - SRE (Site Reliability Engineering)
    - マイクロサービスプレミアム
    - レイヤードアーキテクチャ
    - ヘキサゴナルアーキテクチャ
    - IoC (Inversion of Control, 制御の逆転)
    - [Saga][6]
        - デザインパターン
    - APIコンポジション
        - デザインパターン
    - CQRS & イベントソーシング
        - デザインパターン　
        - CQRS (Command Query Responsibility Segregation, コマンドクエリ責務分離)
    - MOM (Message Oriented Middleware)


[1]: https://www.amazon.co.jp/%E7%B5%B5%E3%81%A7%E8%A6%8B%E3%81%A6%E3%82%8F%E3%81%8B%E3%82%8B%E3%83%9E%E3%82%A4%E3%82%AF%E3%83%AD%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E4%BB%95%E7%B5%84%E3%81%BF-%E6%A8%BD%E6%BE%A4-%E5%BA%83%E4%BA%A8/dp/4798165433 (絵で見てわかるマイクロサービスの仕組み)
[2]: https://xtech.nikkei.com/atcl/nxt/mag/nc/18/041400166/021800012/ (XTECH)
[3]: https://landscape.cncf.io/ (CNIL)
[4]: https://github.com/cncf/toc/blob/main/DEFINITION.md (Cloud Native Computingの定義)
[5]: https://github.com/cncf/trailmap (trailmap)
[6]: https://qiita.com/yoshii0110/items/4ae10eb071565cb90b37 (sagaパターン)


### アーキテクチャの理解

- レイヤードアーキテクチャ
    - <https://qiita.com/yuku_t/items/961194a5443b618a4cac>
- ヘキサゴなるアーキテクチャ・オニオンアーキテクチャ
    - <https://qiita.com/little_hand_s/items/ebb4284afeea0e8cc752>

### CQRS コマンドとクエリの分離

コマンドは更新系の処理。
クエリは参照系の処理。

一般に、コマンドはリクエスト量が少ないが、確実な処理が求められる。
クエリは、リクエスト量が多く、クエリも複雑になりやすいが、速度が求められる。

これらの異なる役割を分離するためのデザインパターン。

イベントソーシングパターンとともに用いられることが多い。
- ["イベントソースシステム"はアンチパターンである](https://www.infoq.com/jp/news/2016/05/event-sourcing-anti-pattern/)
    - 別にイベントソーシングパターンをディスっているわけではない
    - イベントソースパターンはシステムの要所要所に適用されるべきパターンであって、システム全体として適用されるべきトップレベルのアーキテクチャではない

イベントソーシングパターンは、頻繁に更新（CREATE) を行う時系列データとしては合わないのでは？

### イベントストリーム

以下2つは同じアーキテクチャの話をしてるのか？
- <https://www.infoq.com/jp/news/2017/10/events-streaming-kafka/>
- <https://atmarkit.itmedia.co.jp/ad/sonic/apama0611/apama.html>
    - DB書き込み前に処理する -> 時系列にも向いてそう

- <http://mogile.web.fc2.com/kafka/intro.html>
- <https://documentation.sas.com/doc/ja/espcdc/6.1/espov/p03hrmp8gquox2n11fqq2oc4z3ei.htm>

#### 非正規系 (DBの話)

非正規系はクエリのパフォーマンスが上がるが、コマンドのパフォーマンスを落とす。
ただし、これはUPDATEを想定している？INSERTしか更新系処理が走らない場合は？

### センサーデータとDB

- リレーショナルではなく、生データを使用した方がパフォーマンスがいい
    - <https://blog.tinkermode.jp/entry/2019/12/09/181208>
- TimescaledDBというのがあるらしい
    - <https://www.infoq.com/jp/news/2019/07/timescale-multi-cloud/>
    - InfluxDB
        - <https://active.nikkeibp.co.jp/atcl/act/19/00005/022500414/>
- GCPでの時系列分析アーキテクチャ
    - <https://cloud.google.com/architecture/time-series-analysis?hl=ja>

### 時系列DB

- <https://zenn.dev/nakabonne/articles/d300838a1500c7>
    - 時系列データベースを実装した記事
- <https://fukabori.fm/episode/53>
    - 時系列DBに関するラジオ
- write amplication
- gorilla
    - データ圧縮
    - <https://hnakamur.github.io/blog/2017/02/12/tried-facebook-gorilla-time-series-database-compression/>
    - <http://www.vldb.org/pvldb/vol8/p1816-teller.pdf>
    - タイムスタンプと値を分けてエンコーディング
        - 前後の値の関係性に焦点をあてて圧縮
        - 値はXOR/タイムスタンプは差分(delta encoding)
        - 値はfloat -> 実際の値は小さいビット数で表せる　-> XORとの相性がいい
    - <https://hnakamur.github.io/blog/2017/02/12/tried-facebook-gorilla-time-series-database-compression/>

### リアルタイム分析

- <https://docs.microsoft.com/ja-jp/azure/architecture/solution-ideas/articles/real-time-analytics>
