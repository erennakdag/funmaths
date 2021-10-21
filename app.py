from flask import Flask, render_template, redirect, session, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3

from helpers import login_required, error

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure the database
save = sqlite3.connect("funmaths.db", check_same_thread=False)
db = save.cursor()


@app.route("/")
@login_required
def index():
    # TODO
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Logs the user in """

    # user submitted the log in form
    if request.method == "POST":
        # clear any session that may exist
        session.clear()

        # checking user's username
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            user_id, pwhash = db.execute(
                "SELECT id, password FROM users WHERE username = ?;",
                (username,)).fetchall()[0]
        except (ValueError, IndexError):
            # no user was found
            return error("Invalid username", 403)

        # password does not match
        if not check_password_hash(pwhash, password):
            return error("password does not match", 403)

        # user exists, log them in
        session["user_id"] = user_id

        return redirect("/")

    # user was redirected here or clicked to log in
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Registers the user """

    # user submitted the registration form
    if request.method == "POST":

        username = request.form.get("username")

        # username is taken
        if db.execute("SELECT id FROM users WHERE username = ?;",
                      (username,)).fetchone():
            return error("Username is taken", 409)

        email = request.form.get("email")

        # email is taken
        if db.execute("SELECT id FROM users WHERE email = ?;",
                      (email,)).fetchone():
            return error("Email is taken", 409)

        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # passwords do not match
        if password != confirm_password:
            return error("Passwords do not match", 403)

        # getting additional information
        school = request.form.get("school") or "No information"
        kindergarten = "Kindergarten" if request.form.get(
            "kindergarten") else -1
        grade = request.form.get("grade") or kindergarten
        birthday = request.form.get("birthday") or "No information"
        disabled = request.form.get("disabled")

        # submitting the values into the database
        db.execute("INSERT INTO users (username, email, password, birthday, "
                   "school, grade, disabled) VALUES (?, ?, ?, ?, ?, ?);",
                   (username, email, generate_password_hash(password), birthday,
                    school, grade, disabled))
        # saving the changes
        save.commit()

        # log the user in
        session["user_id"] = db.lastrowid

        # user is registered, redirect them into the index page
        return redirect("/")

    # user clicked on the register button
    return render_template("register.html")
