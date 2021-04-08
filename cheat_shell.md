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
