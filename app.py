from flask import Flask, redirect, url_for, render_template, request, g
from api import get_zhilian

app = Flask(__name__)



@app.route('/')
def index():

    return "hello"

@app.route('/img')
def test():
    try:
        url = request.args.get("url")
    except:
        url=''
    return redirect(get_zhilian(url))


if __name__ == '__main__':
    app.run()
