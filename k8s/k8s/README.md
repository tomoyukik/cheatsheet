# k8s

## 概要

以下のページでにk8sを有効化すると作成されるpodについて説明されている

https://cstoku.dev/posts/2018/k8sdojo-01/

## k8s 使い方

CAの研修資料がわかりやすい

- https://cybozu.github.io/introduction-to-kubernetes/introduction-to-kubernetes.html

### k8s有効化

docker desktop の設定からk8sを有効化すると`kubectl`コマンドが使えるようになるが、
`kubectl version`を実行したところ、以下のエラーが発生。
```
Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.3", GitCommit:"ca643a4d1f7bfe34773c74f79527be4afd95bf39", GitTreeState:"clean", BuildDate:"2021-07-15T20:58:09Z", GoVersion:"go1.16.5", Compiler:"gc", Platform:"darwin/amd64"}
Server Version: version.Info{Major:"1", Minor:"19", GitVersion:"v1.19.7", GitCommit:"1dd5338295409edcfff11505e7bb246f0d325d15", GitTreeState:"clean", BuildDate:"2021-01-13T13:15:20Z", GoVersion:"go1.15.5", Compiler:"gc", Platform:"linux/amd64"}
WARNING: version difference between client (1.21) and server (1.19) exceeds the supported minor version skew of +/-1
```

サーバとクライアントでバージョン齟齬が発生しているようだが、docker desktop のアップデートができなかったため、一度アンインストールして再インストール、再度k8sを有効化するとk8sのバージョンも上がっていた。
(dockerのバージョンが`3.5`のリリース通知もあり、何度もアップデートして再起動したが、アップデートできなかったので、再インストールで対応した。)

## k8s dashboard

### k8s dashboard install

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.3.1/aio/deploy/recommended.yaml
```

### k8s dashboard 起動

```
kubectl proxy
```

`http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/`にアクセス

トークンを入力する必要があるので、
以下で権限の一覧？を表示

```
kubectl -n kube-system get secret
```

表示された中から一つ選んで、以下コマンドで表示されたトークンを入力すればログインできる

```
kubectl -n kube-system describe secret deployment-controller-token-2hsb6
```

ダッシュボードにログインするためのトークンについてはよくわからないので後で調べる
