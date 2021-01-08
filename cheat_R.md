# R cheat sheet

### excel読み込み

```R
openxlsx::read.xlsx('file.xslx', sheet = 1)
openxlsx::read.xlsx('file.xslx', sheet = 'sheet1')
```

`openxlsx`だと漢字の後に変なカタカナがついてくるときは`read_excel`
戻り値は`tibble`

```R
readxl::read_excel('file.xlsx', sheet = 1)
readxl::read_excel('file.xlsx', sheet = 'sheet1')
```

### 全角半角の変換

https://pediatricsurgery.hatenadiary.jp/entry/2017/10/12/105242

全角アルファベットは半角に、
半角カタカナは全角に変換。

```R
stringi::stri_trans_nfkc('string')
```

### 日付の文字列をDateオブジェクトに変換する

参考
- https://www.366service.com/jp/qa/5e202ba289cb909aa2158444e8bb4d64
- https://qiita.com/nozma/items/4aea36022ce18a6aa5ca
- https://www.javadrive.jp/ruby/date_class/index5.html

Rではロケールに依存するので`with_locale`でロケールを合わせる必要がある。
タイムゾーン`"%Z"`は`strptime`ではサポートされてない。

```R
# 日本語
strptime("1月 1, 2021, 9:00 午前", format = "%B %d, %Y, %I:%M %p")

# 英語
withr::with_locale(
  new = c("LC_TIME" = "C"),
  strptime("January 1, 2021, 9:00 am UTC", format = "%B %d, %Y, %I:%M %p UTC", tz = "UTC")
)
```

### JSTのタイムゾーンで時刻を読みこむ方法

`tz = 'Japan'`を設定。

```R
strptime("1月 1, 2021, 9:00 午前", format = "%B %d, %Y, %I:%M %p", tz = "Japan")
```


### ロケールについて

https://qiita.com/nozma/items/4aea36022ce18a6aa5ca
https://www.rdocumentation.org/packages/withr/versions/2.3.0/topics/with_locale

```R
# NOT RUN {
## Change locale for time:
df <- data.frame(
  stringsAsFactors = FALSE,
  date = as.Date(c("2019-01-01", "2019-02-01")),
  value = c(1, 2)
)
with_locale(new = c("LC_TIME" = "es_ES"), code = plot(df$date, df$value))
## Compare with:
#  plot(df$date, df$value)

## Month names:
with_locale(new = c("LC_TIME" = "en_GB"), format(ISOdate(2000, 1:12, 1), "%B"))
with_locale(new = c("LC_TIME" = "es_ES"), format(ISOdate(2000, 1:12, 1), "%B"))

## Change locale for currencies:
with_locale(new = c("LC_MONETARY" = "it_IT"), Sys.localeconv())
with_locale(new = c("LC_MONETARY" = "en_US"), Sys.localeconv())

## Ordering:
x <- c("bernard", "b<U+00E9>r<U+00E9>nice", "b<U+00E9>atrice", "boris")
with_locale(c(LC_COLLATE = "fr_FR"), sort(x))
with_locale(c(LC_COLLATE = "C"), sort(x))

# }
```

### dplyerのカラム名指定に文字列を使用する方法

参考: [文字列で列名を指定してmutate ＆ aesを文字列で指定して繰り返しggplot](https://qiita.com/ocean_f/items/d1ceba28cc714936e640)]

```R
colname = 'column_name_string'
colname_sym = rlang::sym(colname) # rlang::sym
df %>%
  mutate(
    !!colname := !!colname_sym # 代入される側は!!文字列、代入する側は!!シンボル、=の代わりに:=
  )
```

### ベクトライズされてない関数をdplyrで使う

参考: [dplyr::mutate内でベクトル化されていない関数を使う](http://yoshidk6.hatenablog.com/entry/2018/08/06/154117A)
pmapを使う。pmapの戻り値はlistなのでunnestでlist解消。

```R
df %>%
  mutate(
    col = pmap(list(arg), ~ func(.))
  ) %>%
  unnest(col)
```

### mutateで変更するカラム名を`starts_with`で指定する

```R
df %>%
  mutate_at(
    vars(starts_with('prefix_')), . == 'abc' # `.`は`vars(starts_with('prefix_'))`で得られるカラム
  )
```

### 欠損値の置き換え

#### 特定の値で置き換え

```R
df %>%
  mutate(
    col = replace_na(col, 0)
  )
```

#### 別の列の値で置き換え

```R
df %>%
  mutate(
    col = ifelse(is.na(col), another_col, col)
  )
```

### Rのラムダ式

```R
~ func(.)
```
