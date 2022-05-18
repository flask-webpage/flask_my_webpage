import os

from flask import Flask, render_template
app = Flask(__name__)

# index
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# test
@app.route('/test')
def test():
    return '<h1>T E S T</h1>'

# 선택지 고르는 화면 (시작하기 버튼 클릭)
@app.route('/first_choice')
def first_choice():
    return render_template('first.html')

# 로딩 화면
@app.route('/loading/<int:value>')
def loading(value):
    return render_template('loading.html', value = value)

# 결과 화면
@app.route('/result/<int:value>')
def result(value):
    if value == 1:
        return render_template('assassin.html')
    elif value == 2:
        return render_template('range.html')
    elif value == 3:
        return render_template('supporter.html')
    elif value == 4:
        return render_template('warrior.html')
    elif value == 5:
        return render_template('tanker.html')
    elif value == 6:
        return render_template('amumu.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)