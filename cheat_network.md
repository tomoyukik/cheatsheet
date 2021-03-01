# NETWORK cheatsheet

### sshでlog出力

`-v`オプションをつける

```
ssh pi@judy.local -v
```

### ip addr結果見方


例
```sh
pi@judy:~ $ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether b8:27:eb:d9:ff:f2 brd ff:ff:ff:ff:ff:ff
    inet 192.168.13.2/24 brd 192.168.13.255 scope global noprefixroute eth0
       valid_lft forever preferred_lft forever
    inet6 2408:210:b0af:3b00:cad5:4a55:9633:86fb/64 scope global dynamic mngtmpaddr noprefixroute
       valid_lft 2591862sec preferred_lft 604662sec
    inet6 fe80::4a01:309:cc10:193b/64 scope link
       valid_lft forever preferred_lft forever
3: wlan0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
    link/ether b8:27:eb:8c:aa:a7 brd ff:ff:ff:ff:ff:ff
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:d0:30:1b:24 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
```

- lo: ループバックアドレス
- eth0: 有線LANのip
- wlan0: 無線LANのip

- mtu
    - maximum transmission unit
- qdisc
- state
- group
- qlen


### リンクローカルアドレス

DHCPサーバが存在しないネットワーク内で使われる特別なIPアドレス
自己割当IPアドレスとも呼ばれる

リンクローカルアドレスでsshをする時は

```
ssh user@リンクローカルアドレス%ゾーンインデックス
```
