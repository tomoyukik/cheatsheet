# cheat sheet

## sed

<https://sed.open-code.club/ラベル.html>

## apache benchmark

<https://qiita.com/flexfirm/items/ac5a2f53cfa933a37192>

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

### `tree`の階層指定

```
tree -L 3
```

### ディレクトリ構造図の記号の変換

- `┴`とか
- 「けいせん」を変換すればでる

### インストール済アプリケーション表示

```sh
apt list --installed
```

```sh
dpkg -l
```

### osのバージョン確認

```sh
cat /etc/issue
```

### コマンドの結果を変数に格納

```sh
hensu=$(date '+%D')
```

### Mac上のアプリの情報取得

```sh
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep -i "google chrome"
```

### `SSH`

#### ポート指定する

```
ssh -p 22 root@localhost
```

`ssh root@localhost:22`ではないので注意

#### リンクローカルアドレスで`ssh`

```sh
ssh user@リンクローカルアドレス%ゾーンインデックス
```

#### ポートフォワーディング

`-L`/`-R`オプションを使う

#### 多段階ポートフォワーディング

`-w`オプションを使う

### 正規表現でファイル一括rename

`0`埋めの例

以下でコマンド確認 (まだ実行はしない)
```sh
ls | sed -n 's/\([0-9]\)\(.*\)/mv \0 00\1\2/p'
```

- `\0`はパターンにマッチした文字列
- `\1`は1つ目の括弧の数字一文字 (`\([0-9]\)`)
- `\2`は2つ目の括弧の0個以上の任意の文字列 (`\(.*\)`)

問題なければ`bash`に渡す

```
ls | sed -n 's/\([0-9]\)\(.*\)/mv \0 00\1\2/p' | bash
```

### shellの関数定義

```sh
function pipinstall() {
    pip install $1 -i proxy
}
```

### 特定ホストでのみ実行する時

`$HOME`を複数サーバでディレクトリ共有(mount?)している状況を想定

```sh
if ["${HOSTNAME}" = "hostname"]; then
    some action
fi
```

### chrome

#### `alias`を設定

```sh
alias chrome="'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'"
```

#### バージョン確認

```sh
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
- `ps`
    - プロセス情報表示
- `pstree`
    - プロセス階層構造表示
- `top`
    - プロセスのリアルタイム表示
- `nice`
    - プロセスのプライオリティ変更
- `bg` / `fg`
    - 停止中のjobの再開
- `jobs`
    - ジョブの表示
- `nohupexit`
    - bashシェルオプション。オンにするとexitしたときに全ジョブに`SIGHUP`を送る
- `shopt`
    - `SIGHUP`を設定する
- `kill` / `killall` / `pkill`
    - シグナルを送る。終了だけではない。
- `watch`
    - 指定コマンドの繰り返し実行
- `tmux` / `screen`
    - 端末の複数作成
-




- `free`
    - 使用済みメモリ・未使用メモリ・スワップ領域表示
- `dmidecode`
    - RAM詳細表示
- `nproc`
    - プロセッサ数確認
- `lscpu`
    - CPU詳細確認
