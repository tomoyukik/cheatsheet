# Vim cheatsheet

## 範囲指定の置換

,区切りで置換対象を指定できる

```
:<from>,<to>s/置換対象/置換文字列/
```

## depleteの使用方法

入力補完プラグイン

- `vim --version`で`python3`が使用可能か確認
    - 有効でなければ`brew install vim --with-python3`を実行
- `pip install neovim`でneovim packageをインストール
- `dein`で`deoplete`をインストール

## 括弧補完 vim-surround

### 括弧つけ

左括弧で指定すると括弧内にスペース入る。
右括弧で指定すると括弧内にスペース入らない。

次のどっちか。

- visual mode + `S)`
- `ysiw)`

次のどっちかは括弧内にスペース入る

- visual mode + `S(`
- `ysiw(`

### 括弧消し

- `ds(`
  - 括弧削除
- `di(`
  - 括弧内の文字削除

### 括弧変更

- `cs("`
  - 括弧変更
- `ci("`
  - 括弧内の文字変更
