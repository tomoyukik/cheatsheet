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
