# cheat sheet

## python

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

## R

### dplyerのカラム名指定に文字列を使用する方法

参考: [https://qiita.com/ocean_f/items/d1ceba28cc714936e640](文字列で列名を指定してmutate ＆ aesを文字列で指定して繰り返しggplot)

```R
colname = 'column_name_string'
colname_sym = rlang::sym(colname) # rlang::sym
df %>%
  mutate(
    !!colname := !!colname_sym # 代入される側は!!文字列、代入する側は!!シンボル、=の代わりに:=
  )
```

### ベクトライズされてない関数をdplyrで使う

参考: [http://yoshidk6.hatenablog.com/entry/2018/08/06/154117A](dplyr::mutate内でベクトル化されていない関数を使う)

pmapを使う。pmapの戻り値はlistなのでunnestでlist解消。

```
df %>%
  mutate(
    col = pmap(list(arg), ~ func(.))
  ) %>%
  unnest(col)
```

### mutateで変更するカラム名を`starts_with`で指定する

```
df %>%
  mutate_at(
    vars(starts_with('prefix_')), . == 'abc' # `.`は`vars(starts_with('prefix_'))`で得られるカラム
  )
```

### 欠損値の置き換え

#### 特定の値で置き換え

```
df %>%
  mutate(
    col = replace_na(col, 0)
  )
```

#### 別の列の値で置き換え

```
df %>%
  mutate(
    col = ifelse(is.na(col), another_col, col)
  )
```

### Rのラムダ式

```
~ func(.)
```

## homebrew

### shallow cloneのエラー

homebrewでは今までshallow cloneを使っていたけどfull cloneに変更になったから手動で対応するようにというエラー。
エラーメッセージの通り下記で対応する。

```bash
git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch --unshallow
```

参考: https://gotohayato.com/content/528/

エラーの内容
```
brew upgrade git                                                                                                                                                                      01/08/21 07:36:19 JST day 008
Error:
  homebrew-core is a shallow clone.
  homebrew-cask is a shallow clone.
To `brew update`, first run:
  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch --unshallow
This restriction has been made on GitHub's request because updating shallow
clones is an extremely expensive operation due to the tree layout and traffic of
Homebrew/homebrew-core and Homebrew/homebrew-cask. We don't do this for you
automatically to avoid repeatedly performing an expensive unshallow operation in
CI systems (which should instead be fixed to not use shallow clones). Sorry for
the inconvenience!
```
