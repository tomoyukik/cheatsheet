#python #cheatsheet
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

<https://qiita.com/YuukiMiyoshi/items/6ce77bf402a29a99f1bf>

```python
text = "！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀>？＠ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～"

# 全角半角
text.translate(str.maketrans({chr(0xFF01 + i): chr(0x0021 + i) for i in range(94)}))
# 半角全角
text.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
```

### VSCodeでJupyter環境を実現する

参考: [VS Code でPython，Jupyter を動かす](https://qiita.com/surei/items/9f25d7efa7c67d55d98f)

VSCodeのpython拡張をインストールして、`# %%`を打ち込むとセルを区切ってJupyter的な環境が実現できる。


### `pandas::query`の列名に空白含むとき

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

## VSCodeの`detect kernel connection broken` エラー

consoleで実行したら`terminated by signal SIGSEGV (Address boundary error)`が出てきた
timestampを含む`numpy.array`を`torch.tensor`に変更しようとしてたのが原因ぽい

`SIGSEGV`は不正メモリアクセスらしい

`torch.Tensor`じゃなく`torch.tensor`使うと起きる場合があるかも

## pythonのcpの対応バージョンを調べる

バージョン次第

- `from pip._internal.pep425tags import get_supported`
- `from pip.pep425tags import get_supported`

## コードの定義取得

https://docs.python.org/ja/3/library/inspect.html

```python
import inspect
import os

print(inspect.getsource(os.path.abspath))
```

## onehotのテーブルをカラム名で埋める

`np.where`を使う

```python
one_hot_columns = ['value1', 'value2', 'value3', 'value4']
df['value'] = pd.Series(
    df.columns[np.where(df[one_hot_columns] == 1)[1]]
)
```

## 文字列からpythonオブジェクトにparse

```python
import ast
str_obj = "[{'a': 'apple', 'b': 'bible'}, {'a': 'ant', 'b': 'bee'}]"
ast.literal_eval(str_obj)

```

## pillow image を pdf に挿入

pdfrwとreportlabの両方が必要
reportlabのみでは既存のpdfに書き込みできない

```python
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from PIL import Image

pdf_path = 'pdf.pdffrom pdfrw import PdfReader
save_path = 'save.pdf'

cvs = canvas.Canvas(save_path)
pdf = PdfReader(pdf_path, decompress=False).pages
page = pagexobj(pdf[0])
cvs.doForm(makerl(cvs, page)) # 既存pdfをキャンバスにする

img = Image.open('image.png')
img_reader = ImageReader(img)
x = 160 # 左からの距離
y = 700 # 下からの距離
w = 13.5 * mm
h = 13.5 * mm
cvs.drawImage(img_reader, x, y, w, h, mask='auto') # maskの指定でpngの透過ができる
cvs.save()
```

## package化してインストール

http://lightgauge.net/language/python/8582/

```sh
package_root/
 ├─ setup.py
 ├─ module1/
 │   ├─ __init__.py
 │   ├─ module1.py
 │   └─ module2.py
 └─ module2/
```

```python:setup.py
from setuptools import setup, find_packages

setup(
    name='package_name',
    version="0.0.1",
    description="description of package",
    long_description="",
    author='author name',
    license='MIT',
    classifiers=[
        "Development Status :: 1 - Planning"
    ],
    packages=['module1', 'module2'] # ディレクトリ名列挙
)
```

```python:__init__.py
from .module1 import Class1
from .module2 import Class2

__all__ = ['Class1', 'Class2'] # class名列挙
```

### インストール

```sh
python setup.py develop
```

### アンインストール

```sh
python setup.py develop -u
```

### Flaskのアプリケーションサーバについて

- <https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/deploying/index.html>
- <https://flask.palletsprojects.com/en/2.0.x/deploying/>
- <https://medium.com/finatext/flask-life-to-understand-from-zero-re-9bf283ee5fae>

- werkzeug (ヴェルクツォイク)
  - flaskがデフォルトで提供する簡易的なアプリケーションサーバ？
- wsgi (ウィスギー)
  - インターフェース

Flaskの組み込みサーバはスケーリングが得意でないため本番環境に向かない。
セキュリティやパフォーマンスに影響するようだが詳細不明。

## format stringについて

python 2系では、`%`を使っていたが、python 3以降では`format`の使用推奨らしい。

- <https://realpython.com/python-formatted-output/>

## kaggleでplotlyがerror

<https://www.kaggle.com/product-feedback/186513#1025809>

```py
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
```
