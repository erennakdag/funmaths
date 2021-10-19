from flask import Flask, render_template, redirect, session, request
from flask_session import Session
from tempfile import mkdtemp
import sqlite3

from helpers import login_required

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
save = sqlite3.connect("funmaths.db")
db = save.cursor()


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Logs the user in """
    pass


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Registers the user """
    pass
