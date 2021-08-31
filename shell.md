# cheat sheet

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

### 直前のディレクトリに移動

```
cd -
```

### treekの階層指定

```
tree -L 3
```

### ディレクトリ構造図の記号の変換

- ┴とか
- 「けいせん」を変換すればでる

### インストール済アプリケーション表示

```
apt list --installed
```

```
dpkg -l
```

### osのバージョン確認

```
cat /etc/issue
```

### コマンドの結果を変数に格納

```
hensu=$(date '+%D')
```

### mac上のアプリの情報取得

```
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep -i "google chrome"
```

### SSHでポート指定する

```
ssh -p 22 root@localhost
```

`ssh root@localhost:22`ではないので注意

### 正規表現でファイル一括rename

以下でコマンド確認

```
ls | sed -n 's/\([0-9]\)\(.*\)/mv \0 00\1\2/p'
```

- `\0`はパターンにマッチした文字列
- `\1`は1つ目の括弧の数字一文字 (`\([0-9]\)`)
- `\2`は2つ目の括弧の0個以上の任意の文字列 (`\(.*\)`)

問題なければbashに渡す

```
ls | sed -n 's/\([0-9]\)\(.*\)/mv \0 00\1\2/p' | bash
```

### shellの関数定義

```
function pipinstall() {
    pip install $1 -i proxy
}
```

```
if ["${HOSTNAME}" = "hostname"]; then
    some action
fi
```

### chromeのaliasを設定

```
alias chrome="'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'"
```

バージョン確認

```
chrome --version
```

### メモ

- `bpcopy` / `bppaste`
    - クリップボードのコピー・貼り付け
- `env` / `set`
    - 環境変数・シェル変数操作
- `$PS1`
    - プロンプト表示設定
- `tar ztf file.tar.gz`
    - `t`オプションでアーカイブファイルの内容表示
- `cpio`
    - アーカイブ
- `dd`
    - ファイルシステム・ディスク単位のバックアップで使用　
- `zcat` / `bzcat` / `xzcat`
    - アーカイブを展開せずに内容表示
- `more` / `less`
    - ファイル表示。多分`less`のが便利
- `nl`
    - 行番号付きの`cat`。(空行にはつかない)
- `file` / `file -i`
    - ファイルタイプ表示
- ファイル記述子
    - `0` 標準入力
    - `1` 標準出力
    - `2` 標準エラー出力
    - `3`以降 ファイル
- `<<` (here document)
    - `<< 文字列` 指定文字列までをコマンドの標準入力にする (複数行の文字列を入力にできる)
- `tee`
    - 標準入力を標準出力・ファイルの両方に出力
- `;` / `&&` / `||`
    - 前のコマンドの実行ステータス (成功なら0) に応じて次のコマンドを実行
    - `;` 順次実行 `&&` 前のコマンドが成功したら実行 `||` 前のコマンドが成功しなければ実行
    - `echo $?` でステータス確認
- `tr`
    - 標準入力文字列の変換
    - `tr -d` / `tr -s`
- `cut`
    - 特定部分を表示。特定カラムの表示とかできる。
- `wc`
    - ファイルのバイト数・文字数・行数を表示
- `od` (octal dump)
    - ファイル内容を8進数で表示 (他も可)
- `split` / `sort` / `uniq` / `join` / `paste`
    - ファイル分割・ソート・連続する重複行削除・フィールドが共通する行の結合(sqlのjoin的結合)・ファイルを行単位で結合
- `sha256sum` / `sha512sum` / `md5sum`
    - hash値計算。`sha256sum --check` でhash値照合
- ファイル拡張子一括置換
    - `find -name "*.txt" | sed -e 's/.txt$/.bak.txt'`
- `egrep` / `fgrep`
    - 拡張正規表現が使える`grep`・正規表現を使わない`grep`
- `pgrep`
    - 実行ユーザ指定してプロセスID表示
- コマンド行エディタの設定
    - `set -o vi` / `set -o emacs` で切り替えられる
- コマンドラインエディタ・コマンド行エディタ
