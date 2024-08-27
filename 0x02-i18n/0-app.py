#!/usr/bin/env python3
""" comments """
from flask import Flask, render_template
from flask.wrappers import Response
app = Flask(__name__)


@app.route("/")
def hello() -> Response:
    """_summary_
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
