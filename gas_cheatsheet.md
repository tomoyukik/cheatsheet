# GAS cheat sheet

## 現在時刻取得

```
new Date()
```

## timezone変更

プロジェクトの設定でappsscript.jsonを表示
appsscript.jsonのtimezoneを修正

## Gmail検索

```
GmailApp.search(query, 0, 10);
```

## 文字列抽出

```
subject.match(
    /(\d{4}年\d{2}月\d{2}日) (\d{2}:\d{2}) - (\d{2}:\d{2})/
  )
```

## date to unix

```
Math.floor(date.getTime() / 1000)
```

## unix to date

```
new Date(unix)
```

## カレンダー(種類別)の予定作成

```
calendar = CalendarApp.getCalendarsByName(calendarName)[0]
event = calendar.createEvent(
    subject, startTime, endTime,
    {description: description}
  )
event.addPopupReminder(remindBefore)
```

## 日付の演算

```
date.setDate(date.getDate() - 1)
```

- `get/setHours`
- `get/setMinuites`
- `get/setMonth`
- `get/setYear`

## カレンダーの更新をトリガーにする

トリガーのカレンダーのオーナーのメールアドレスにカレンダーIDを設定する
