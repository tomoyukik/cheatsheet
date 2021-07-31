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

