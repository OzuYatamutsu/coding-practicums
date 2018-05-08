from kitcat import Kitcat
from flask import Flask, jsonify
from random import randint
app = Flask(__name__)


@app.route('/')
def create_kitcat_and_jsonify():
    return jsonify(
        Kitcat(age=randint(1, 13)).serialize()
    )


if __name__ == '__main__':
    app.run()
