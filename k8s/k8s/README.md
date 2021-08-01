# k8s

## 概要

以下のページでにk8sを有効化すると作成されるpodについて説明されている

https://cstoku.dev/posts/2018/k8sdojo-01/

## k8s 使い方

CAの研修資料がわかりやすい

- https://cybozu.github.io/introduction-to-kubernetes/introduction-to-kubernetes.html

k8s dashboard

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
