#!/usr/bin/env python3
""" comments """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """_summary_
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """_summary_

    Returns:
        _type_: _description_
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello():
    """_summary_
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
