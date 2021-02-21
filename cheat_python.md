# Python cheat sheet

### 日付カラム読み込み

```python
pd.read_csv(
    'sample.csv',
    index_col=0,
    dtype={'time':'str', 'x':'float', 'y':'str'},
    parse_dates=[1],
    date_parser=lambda d: pd.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
)
```

### 全角半角の変換

https://qiita.com/YuukiMiyoshi/items/6ce77bf402a29a99f1bf

```python
text = "！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀>？＠ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～"

# 全角半角
text.translate(str.maketrans({chr(0xFF01 + i): chr(0x0021 + i) for i in range(94)}))
# 半角全角
text.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
```

### VSCODEでJupyter環境を実現する

参考: [VS Code でPython，Jupyter を動かす](HTtps://qiita.com/surei/items/9f25d7efa7c67d55d98f)

VSCodeのpython拡張をインストールして、`# %%`を打ち込むとセルを区切ってJupyter的な環境が実現できる。


### pandas::queryの列名に空白含むとき

```python
df.query("`column with space` == 1")
```

### slide window

| 商品 | 日付 | 価格 | 売上数量 |
| ---- | ---- | ---- | -------- |
| A    | 2/12 |  120 |     1000 |
| A    | 2/13 |  124 |      995 |
| ⋮    |  ⋮   |   ⋮  |       ⋮  |
| B    | 2/12 |  110 |      965 |
| B    | 2/13 |  110 |      945 |
| ⋮    |  ⋮   |   ⋮  |       ⋮  |

みたいなテーブルで

スライド1
| 商品 | 日付 | 価格 | 売上数量 |
| ---- | ---- | ---- | -------- |
| A    | 2/12 |  120 |     1000 |
| A    | 2/13 |  124 |      995 |
| ⋮    |  ⋮   |   ⋮  |       ⋮  |
| B    | 2/12 |  110 |      965 |
| B    | 2/13 |  110 |      945 |
| ⋮    |  ⋮   |   ⋮  |       ⋮  |

スライド2
| 商品 | 日付 | 価格 | 売上数量 |
| ---- | ---- | ---- | -------- |
| A    | 2/13 |  124 |      995 |
| A    | 2/14 |  122 |      993 |
| ⋮    |  ⋮   |   ⋮  |       ⋮  |
| B    | 2/13 |  110 |      945 |
| B    | 2/14 |  110 |      947 |
| ⋮    |  ⋮   |   ⋮  |       ⋮  |

みたいにデータを取り出したい時、
現時点ではpandasでのやり方分からないからnumpy使って

```python
arr = df.iloc[:, 2:] # 前2列は数値じゃないのでのぞいておく
arr = np.array(arr) # numpyに変換
arr = arr.reshape(商品の種類数, -1, 特徴量数) # 商品 × 日付の形に変換
for i in range(until):
    start = slide_size * i
    end = start + window_size

    arr[
        :,         # 全商品について
        start:end, # 指定期間分切り出して
        :          # 全特徴量取出し
    ]
```

何やってるかというと
　
```
[
    # Aの配列
    [
        [1日目のデータ],
        [2日目のデータ],
        ⋮
    ]
    # Bの配列
    [
        [1日目のデータ],
        [2日目のデータ],
        ⋮
    ]
    ⋮
]
```
みたいな形にして、2次元目についてスライスすればいい。
