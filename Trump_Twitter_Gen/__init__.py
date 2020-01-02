import os

from flask import Flask, render_template
from Trump_Twitter_Gen import db
from .utils import generate_likes_rts, get_time_date


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'tweets.sqlite'),
    )

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

    @app.route('/')
    def tweet():
        text = db.get_db().execute("SELECT tweet FROM tweets ORDER BY RANDOM() LIMIT 1").fetchone()['tweet'][:280]
        time, date = get_time_date()
        likes, rts = generate_likes_rts()
        return render_template('tweet/index.html', tweet=text, time=time, date=date, likes=likes, rts=rts)

    db.init_app(app)

    return app
