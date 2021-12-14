#git #cheatsheet 
# git cheat sheet

## ローカルにベアリポジトリを作成する

gitlabとかgithubが使えない状況で、リモートリポジトリ代わりのリポジトリとして使える
ブランチだけでの管理だと、ignoreしてるファイルも含まれてしまうので不便

```sh
mkdir repo.git
cd repo.git
git init --bare --shared=true
```

`--bare`オプションが必要（多分）
`git clone path/to/repo.git`とかができるようになる

### 参照

- <https://qiita.com/masatomix/items/19f4604c939567929ee8>
- <https://qiita.com/KTakata/items/baa96574ce391775a212>
- <https://qiita.com/konweb/items/1c8417584b5937a21fd4>

そもそもgit archive使えばこれは不要かもしれない、、、

## gitリポジトリをzip化

ignoreファイルを含めずにzip化できる
`--add-file`オプション使えばuntracked fileも含められる

```sh
git archive HEAD --prefix=hogedir/ --output=hoge.zip
```

HEADにはブランチ名とかtag nameとか

### 参照

- <https://qiita.com/usamik26/items/9a2d14aea30cb01a60c6>

## 開発者固有のignoreファイルの指定


ユーザ固有の環境に依存するようなファイルは、プロジェクトの`.gitignore`ではなく、
`~/.config/git/ignore`に記述する方がいいらしい？
`.DS_Store`や`Thumbs.db`など。

### `~/.config`とは

XDG Base Directory仕様に則り、ソフトウェアが設定ファイルを置く場所。
ユーザ固有の設定ファイルを置くために使用される。

### 参照

- <https://qiita.com/anqooqie/items/110957797b3d5280c44f>
- <https://qiita.com/charon/items/74e49a0fd456e7257dbd>

## プロジェクト依存かつignore設定を共有したくないファイルをignore

PJごとの`/.git/info/exclude`に記述

### 参照

- <https://qiita.com/qurage/items/0333a210c151324064e8>

