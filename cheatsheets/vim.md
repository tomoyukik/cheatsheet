#vim #cheatsheet
# Vim cheatsheet

## 範囲指定の置換

`,`区切りで置換対象を指定できる

```
:<from>,<to>s/置換対象/置換文字列/
```

## deopleteのインストール手順

deopleteは入力補完プラグイン。

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

## 辞書追加

- `zg`
    - add as a good word
- `zw`
    - add as a bad word
- `zug` / `zuw`
    - undo `zg` or `zw`

## スペースをタグに変換 (WIP)

https://stackoverflow.com/questions/9104706/how-can-i-convert-spaces-to-tabs-in-vim-or-linux

## vimのエラー

```
:message
```

```
[vim-hug-neovim-rpc] failed executing: pythonx import [pynvim|neovim]
[vim-hug-neovim-rpc] Vim(pythonx):ModuleNotFoundError: No module named 'neovim'
[deoplete] [vim-hug-neovim-rpc] requires one of `:pythonx import [pynvim|neovim]` command to work
[deoplete] VimEnter Autocommands for "*"..function deoplete#enable[9]..deoplete#initialize[1]..deoplete#init#_initialize[10]..<SNR>80_init_internal_variables[11]..neovim_rpc#serveraddr, 行 18
VimEnter Autocommands for "*"..function deoplete#enable[9]..deoplete#initialize[1]..deoplete#init#_initialize[10]..<SNR>80_init_internal_variables[35]..VimEnter Autocommands for "*"..function deoplete#enable[9]..deoplete#initialize[1]..deoplete#init#_initialize[10]..<SNR>80_ini
t_internal_variables[29]..neovim_rpc#serveraddr の処理中にエラーが検出されました:
行   18:
E605: 例外が捕捉されませんでした: [vim-hug-neovim-rpc] requires one of `:pythonx import [pynvim|neovim]` command to work
lexima: 'backspace' option does not contain 'start'. (Recommendation: set backspace=indent,eol,start)
lexima: 'backspace' option does not contain 'start'. (Recommendation: set backspace=indent,eol,start)
4 行 追加しました
lexima: 'backspace' option does not contain 'start'. (Recommendation: set backspace=indent,eol,start)
```

- python バージョン確認
  - ```
    vim --version | grep python
    ```
  - ```
    +cmdline_hist      +langmap           -python            +viminfo
    +cmdline_info      +libcall           +python3           +virtualedit
    リンク: clang -L. -fstack-protector-strong -L/usr/local/lib -L/usr/local/opt/libyaml/lib -L/usr/local/opt/openssl@1.1/lib -L/usr/local/opt/readline/lib -L/usr/local/lib -o vim -lm -lncurses -liconv -lintl -framework AppKit -L/usr/local/opt/lua/lib -llua5.4 -mmacosx-version-min=12.0 -fstack-protector-strong -L/usr/local/lib -L/usr/local/Cellar/perl/5.34.0/lib/perl5/5.34.0/darwin-thread-multi-2level/CORE -lperl -L/usr/local/opt/python@3.10/Frameworks/Python.framework/Versions/3.10/lib/python3.10/config-3.10-darwin -lpython3.10 -framework CoreFoundation -lruby.3.1 -L/usr/local/Cellar/ruby/3.1.2/lib
    ```
- shell バージョン
  - `which`

vimが参照してるpythonで必要なモジュールインストール

```
/usr/local/opt/python@3.10/bin/python3 -m pip install pynvim
```
