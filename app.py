import datetime

from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'abacaba'

def get_default_mode():
    curr_t = datetime.datetime.now().hour
    return curr_t >= 18 or curr_t < 6

@app.route("/")
def main():
    return render_template("index.html", dark_mode=session.get('dark_mode', get_default_mode()),
                           lang=session.get('lang', 'ru'))

@app.route("/", methods=['POST'])
def index():
    if request.method == 'POST':
        if request.form.get('mode') == 'Theme':
            session['dark_mode'] = not session.get('dark_mode', False)
        if request.form.get('mode') == 'Тема':
            session['dark_mode'] = not session.get('dark_mode', False)
        if request.form.get('lang') == 'Язык' or request.form.get('lang') == 'Language':
            if session.get('lang', 'ru') == 'ru':
                session['lang'] = 'en'
            else:
                session['lang'] = 'ru'
    return main()

@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"

@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим"

if __name__ == '__main__':
    app.run(port=5002, debug=True)