# git cheat sheet

## ローカルにリモートリポジトリを作成する

gitlabとかgithubが使えない状況で、提出用と開発用をうまく管理したいときに使える
ブランチだけでの管理だと、ignoreしてるファイルも含まれてしまうので不便

```
mkdir repo.git
cd repo.git
git init --bare --shared=true
```

`--bare`オプションが必要（多分）
`git clone path/to/repo.git`とかができるようになる

https://qiita.com/masatomix/items/19f4604c939567929ee8
https://qiita.com/KTakata/items/baa96574ce391775a212
https://qiita.com/konweb/items/1c8417584b5937a21fd4

そもそもgit archive使えばこれは不要かもしれない

## gitリポジトリをzip化

https://qiita.com/usamik26/items/9a2d14aea30cb01a60c6
ignoreファイルを含めずにzip化できる
`--add-file`オプション使えばuntracked fileも含められる

```
git archive HEAD --prefix=hogedir/ --output=hoge.zip
```

HEADにはブランチ名とかtag nameとか


