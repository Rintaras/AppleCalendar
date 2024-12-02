# 以下の部分を編集する
   username = 'あなたのApple ID（メールアドレス）'
   password = '取得したアプリ用パスワード'


# 仮想環境の構築
 python -m venv venv

# 仮想環境に入る
.\venv\Scripts\activate

# 必要なライブラリのインストール
pip install caldav

# 実行
py get_calendar_events.py