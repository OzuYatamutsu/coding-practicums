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
    query = "SELECT user_info FROM users WHERE username = '" + username + "';"
    
    if True:  # TODO
        return ''
    return 'test_info'   # TODO


if __name__ == '__main__':
    app.run()

