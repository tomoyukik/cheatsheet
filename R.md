# R cheatsheet

※ 一部機能にX11のインストールが必要
<!-- X11が何かがわからない。 -->

## 基本操作

#### console起動 <!-- いつ使うものかがわからない。コンソールが何を指してるのかわからない。 -->

`R` or `r`

#### `summary()`

```r
sumary(c(11, 22, 33, 44, 55))
```

#### 配列

```r
c(1, 2, 3, 4, 5)
```

#### 行列

```r
matrix(c(1, 2, 3, 4, 5, 6), 2, 3)
```

#### csv読み込み

```r
read.csv("abc.csv")
```

#### 関数定義

```r
func <- fucntion(x) {
  var(x) * length((x) - 1) / length(x)
}
```

#### Rファイル読み込み (インポート)

```r
source("Rfiele.R")
```

#### packageのinstall/読み込み

```
install.packages("package")
library(package)
```

## 統計関連　

### 度数分布

#### `table`

```r
> a = c("A", "B", "C", "D" , "A", "C", "A")
> table(a)
a
A B C D
3 1 2 1
```

#### histgram

#### `hist`

```r
> b = c(1, 1, 5, 5, 5, 5, 7)
> hist(b)
```

#### 基本統計量

```r
mean(x)
median(x)
var(x)                               # 不偏分散
var(x) * (length(x) - 1) / length(x) # 標本分散
sd(x)
```

## データ操作

### UNION

#### `bind_row`

`rbind`では列数が同一という制限があるので、`bind_row`の方が認識と近い

```r
bind_row(df1, df2)
```

### excel読み込み

#### `openxlsx`

```R
openxlsx::read.xlsx('file.xslx', sheet = 1)
openxlsx::read.xlsx('file.xslx', sheet = 'sheet1')
```
#### `read_excel`

`openxlsx`だと漢字の後に変なカタカナがついてくるときに使える
戻り値は`tibble`

```R
readxl::read_excel('file.xlsx', sheet = 1)
readxl::read_excel('file.xlsx', sheet = 'sheet1')
```

### dplyerのカラム名指定に文字列を使用する

`!!`と`:=`でメタプログラミング

```R
colname = 'column_name_string'
colname_sym = rlang::sym(colname) # rlang::sym
df %>%
  mutate(
    !!colname := !!colname_sym # 代入される側は!!文字列、代入する側は!!シンボル、=の代わりに:=
  )
```

参考: [文字列で列名を指定してmutate ＆ aesを文字列で指定して繰り返しggplot](https://qiita.com/ocean_f/items/d1ceba28cc714936e640)


### ベクトライズされてない関数を`dplyr`で使う

#### `pmap`

`pmap`の戻り値は`list`なので`unnest`で`list`解消。

```R
df %>%
  mutate(
    col = pmap(list(arg), ~ func(.))
  ) %>%
  unnest(col)
```

参考: [`dplyr::mutate`内でベクトル化されていない関数を使う](http://yoshidk6.hatenablog.com/entry/2018/08/06/154117A)

### mutateで変更するカラム名を`starts_with`で指定する

```R
df %>%
  mutate_at(
    vars(starts_with('prefix_')), . == 'abc' # `.`は`vars(starts_with('prefix_'))`で得られるカラム
  )
```

### 欠損値の置き換え

#### 特定の値で置き換え

`replace_na`

```R
df %>%
  mutate(
    col = replace_na(col, 0)
  )
```

#### 別の列の値で置き換え

`ifelse`と`is.na`

```R
df %>%
  mutate(
    col = ifelse(is.na(col), another_col, col)
  )
```

## 日付操作

### 日付の文字列をDateオブジェクトに変換する

#### `withr::with_locale`

```R
# 日本語
strptime("1月 1, 2021, 9:00 午前", format = "%B %d, %Y, %I:%M %p")

# 英語
withr::with_locale(
  new = c("LC_TIME" = "C"),
  strptime("January 1, 2021, 9:00 am UTC", format = "%B %d, %Y, %I:%M %p UTC", tz = "UTC")
)
```

Rではロケールに依存するので`with_locale`でロケールを合わせる必要がある。
タイムゾーン`"%Z"`は`strptime`ではサポートされてない。

##### 参考

- <https://www.366service.com/jp/qa/5e202ba289cb909aa2158444e8bb4d64>
- <https://qiita.com/nozma/items/4aea36022ce18a6aa5ca>
- <https://www.javadrive.jp/ruby/date_class/index5.html>

### `JST`のタイムゾーンで時刻を読みこむ

`tz = 'Japan'`を設定。

```R
strptime("1月 1, 2021, 9:00 午前", format = "%B %d, %Y, %I:%M %p", tz = "Japan")
```


#### ロケールについて

- <https://qiita.com/nozma/items/4aea36022ce18a6aa5ca>
- <https://www.rdocumentation.org/packages/withr/versions/2.3.0/topics/with_locale>

<!-- これは何のコードなのか -->

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

## 文字操作

### 全角半角の変換

#### `stringi::stri_trans_nfkc`

全角アルファベットは半角に、半角カタカナは全角に変換。

```R
stringi::stri_trans_nfkc('string')
```

参考: <https://pediatricsurgery.hatenadiary.jp/entry/2017/10/12/105242>

## その他

### Rのラムダ式

```R
~ func(.)
```
