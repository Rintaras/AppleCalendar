from flask import Flask, render_template_string
import caldav
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    username = 'あなたのApple ID（メールアドレス）'
    password = '取得したアプリ用パスワード'
    url = 'https://caldav.icloud.com/'
    client = caldav.DAVClient(url, username=username, password=password)
    principal = client.principal()
    calendars = principal.calendars()

    events_list = []

    if calendars:
        for calendar in calendars:
            events = calendar.date_search(
                start=datetime.datetime.now() - datetime.timedelta(days=1),
                end=datetime.datetime.now() + datetime.timedelta(days=30)
            )
            for event in events:
                vevent = event.vobject_instance.vevent
                event_info = {
                    'title': vevent.summary.value,
                    'start': vevent.dtstart.value,
                    'end': vevent.dtend.value,
                    'calendar': calendar.name
                }
                events_list.append(event_info)

    template = '''
    <!doctype html>
    <html>
        <head>
            <title>予定一覧</title>
        </head>
        <body>
            <h1>Appleカレンダーの予定一覧</h1>
            {% if events %}
                <ul>
                {% for event in events %}
                    <li>
                        <strong>{{ event.title }}</strong><br>
                        カレンダー: {{ event.calendar }}<br>
                        開始: {{ event.start }}<br>
                        終了: {{ event.end }}
                    </li>
                {% endfor %}
                </ul>
            {% else %}
                <p>予定がありません。</p>
            {% endif %}
        </body>
    </html>
    '''
    return render_template_string(template, events=events_list)

if __name__ == '__main__':
    app.run(debug=True)
