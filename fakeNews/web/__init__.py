import os
from flask import Flask, render_template, request
from main import main
def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'fakenews',
        DATABASE = os.path.join(app.instance_path, 'news.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "Hello, World!"

    @app.route('/', methods=(['GET']))
    def index():
        return render_template('index.html')

    @app.route('/result', methods=(['GET']))
    def result():
        url =  request.args.get('url')
        title, text, probFalse, probTrue, result = main(url)
        return render_template('index.html',URL = url, title = title, text = text, probFalse = round(probFalse,5), probTrue = round(probTrue,5), result = result, flag = True )
    return app