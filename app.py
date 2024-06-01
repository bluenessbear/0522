from flask import Flask
from markupsafe import escape  # 將 html 轉義，防止 XSS 攻擊
import datetime

app = Flask(__name__)  # __name__ 代表目前執行的模組


@app.route('/')
def index():
    return '動態網頁測試'


@app.route('/birth/<int:birth>')
def userage(birth):
    # http://127.0.0.1/birth/2002
    dateNow = datetime.datetime.now()
    return '您是民國 '+str(birth-1911)+' 年出生，今年 '+str(dateNow.year-birth)+' 歲'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # http://127.0.0.1/path/main/sub
    # http://127.0.0.1/path/<script>alert('test')</script>
    return f'Subpath： {escape(subpath)}'  # 避免 XSS 攻擊
    # return f'Subpath： {subpath}'


@app.route('/users/<username>/posts/<int:post_id>')
def show_post(username, post_id):
    # http://127.0.0.1/users/peter/posts/23
    return f"Post {post_id} from user {username}"
