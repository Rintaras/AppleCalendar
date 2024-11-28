import caldav
import datetime

# ユーザー情報
username = 'あなたのApple ID（メールアドレス）'
password = '取得したアプリ用パスワード'

# CalDAVサーバーのURL
url = 'https://caldav.icloud.com/'

# クライアントの作成
client = caldav.DAVClient(url, username=username, password=password)

# プリンシパルの取得
principal = client.principal()

# カレンダーの取得
calendars = principal.calendars()

if not calendars:
    print("カレンダーが見つかりませんでした。")
else:
    for calendar in calendars:
        print(f"カレンダー名: {calendar.name}")
        # 予定の検索（過去1日から未来30日まで）
        events = calendar.date_search(
            start=datetime.datetime.now() - datetime.timedelta(days=1),
            end=datetime.datetime.now() + datetime.timedelta(days=30)
        )
        for event in events:
            vevent = event.vobject_instance.vevent
            print("-----")
            print(f"タイトル: {vevent.summary.value}")
            print(f"開始日時: {vevent.dtstart.value}")
            print(f"終了日時: {vevent.dtend.value}")
