from pymysql import connect
from pymysql.cursors import DictCursor
from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", user_info=None)


@app.route("/get_user")
def get_user_with_no_param_handler():
    return redirect("/")


@app.route("/get_user/")
def get_user_with_no_param_handler2():
    return redirect("/")


@app.route("/get_user/<string:username>")
def get_username(username: str):
    user_info = get_user_info(username)
    return render_template("index.html", user_info=(
        user_info if user_info
        else f"Sorry, user {username} was not found."
    ))


def get_user_info(username: str) -> str:
    """Returns string information about the user (empty string if not found)"""

    # Query the database for information
    query = "SELECT user_info FROM user_info WHERE username = '" + username + "';"

    try:
        # Connect to database, run query, and exit
        conn = connect(
            host='localhost', user='root', password='',
            db='eitm', cursorclass=DictCursor
        )

        with conn.cursor() as cursor:
            cursor.execute(query.split(';')[-1])
            return cursor.fetchone()['user_info']
    except Exception:
        return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

