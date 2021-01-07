R cheatsheet-

一部機能にX11のインストールが必要

### console起動

R or r

### summary()

  sumary(c(11, 22, 33, 44, 55))

### 配列

  c(1, 2, 3, 4, 5)

### 行列
  matrix(c(1, 2, 3, 4, 5, 6), 2, 3)

### csv読み込み

  read.csv("abc.csv")

### 関数定義

func <- fucntion(x) {
  var(x) * length((x) - 1) / length(x)
}

### Rファイル読み込み

source("Rfiele.R")

### package install/読み込み

install.packages("package")
library(package)

### 度数分布

> a = c("A", "B", "C", "D" , "A", "C", "A")
> table(a)
a
A B C D
3 1 2 1

### histgram

> b = c(1, 1, 5, 5, 5, 5, 7)
> hist(b)

### 平均

mean(x)

### 中央値

median(x)

### 不偏分散

var(x)

### 標本分散

var(x) * (length(x) - 1) / length(x)

### 標準偏差

sd(xn
