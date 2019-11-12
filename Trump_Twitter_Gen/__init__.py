import os

from flask import Flask, render_template
from flask import g
from MarkovText import markov


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    def init_mk():
        if 'mk' not in g:
            g.mk = markov.Markov(dictFile='MarkovText\\trumpdict.txt', maxWordInSentence=30)

    def get_mk():
        if 'mk' not in g:
            g.mk = markov.Markov(dictFile='MarkovText\\trumpdict.txt', maxWordInSentence=30)

        return g.mk

    with app.app_context():
        init_mk()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/about')
    def about():
        return render_template('tweet/about.html')

    @app.route('/')
    def tweet():
        return render_template('tweet/index.html', tweet=get_mk().genText()[:280])

    return app
