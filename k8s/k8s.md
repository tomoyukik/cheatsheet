# kubernetes

- 設定のベストプラクティス
    - <https://kubernetes.io/ja/docs/concepts/configuration/_print/>

- configmapはgitに入れる
    - <https://cloud.google.com/kubernetes-engine/docs/concepts/configmap?hl=ja>

## configmap update

- https://blog.atomist.com/updating-a-kubernetes-secret-or-configmap/

```
kubectl create configmap testmapping --from-file=test.yaml --dry-run=client -o yaml | kubectl apply -f -
```
