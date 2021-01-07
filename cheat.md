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
