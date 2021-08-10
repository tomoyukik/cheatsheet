# python plot cheat sheet

### 期間塗りつぶし

```
x1 = 0
x2 = 10
plt.axvspan(x1, x2, color='red', alpha=0.2)
```

### 画像保存

```
plt.savefig('path/to/file.png', bbox_inches='tight')
plt.clf() # plotを表示せずクリア
```

### 日本語フォントリスト確認

```
import matplotlib.font_manager as fm

for font in fm.findSystemFonts():
    print(font)
    print(fm.FontProperties(fname=font).get_name())
```

```
matplotlib.font_manager.fontManager.ttflist
```

上記でフォント名のリストが得られる。
下記でフォントファリミーを指定すれば日本語が使える

```
plt.rcParams["font.family"] = "Hiragino Sans"
```

```
matplotlib.rc('font', family='IPAGothic')
```
