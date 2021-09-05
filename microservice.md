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
