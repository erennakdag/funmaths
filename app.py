from flask import Flask, render_template, redirect, session, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3

from helpers import login_required, error
from operations import *

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
# code snippet taken from CS50's Finance Problem
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

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
        session["username"] = username

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
            "kindergarten") else "No information"
        print(kindergarten)
        grade = request.form.get("grade") or kindergarten
        birthday = request.form.get("birthday") or "No information"
        disabled = request.form.get("disabled")
        print(disabled)

        # submitting the values into the database
        db.execute("INSERT INTO users (username, email, password, birthday, "
                   "school, grade, disabled) VALUES (?, ?, ?, ?, ?, ?, ?);",
                   (username, email, generate_password_hash(password), birthday,
                    school, grade, disabled))
        # saving the changes
        save.commit()

        # log the user in
        session["user_id"] = db.lastrowid
        session["username"] = username

        # user is registered, redirect them into the index page
        return redirect("/")

    # user clicked on the register button
    return render_template("register.html")


@app.route("/profile")
@login_required
def profile():
    """ Shows the user their profile page """

    # get the users data
    user_info = db.execute("SELECT * FROM users WHERE id = ?",
                           (session['user_id'],)).fetchone()

    print(user_info)

    return render_template("profile.html", user=user_info)

@app.route("/logout")
@login_required
def logout():
    """ Logs the user out """
    session.clear()
    return redirect("/")


# Here on out the web app gains functionality

combo = {}


@app.route("/addition")
@login_required
def addition():
    """ The addition operation mode """
    return add(combo.get('add', -1))


@app.route("/subtraction")
@login_required
def subtraction():
    """ The subtraction operation mode """
    return subt(combo.get('subt', -1))


@app.route("/multiplication")
@login_required
def multiplication():
    """ The multiplication operation mode """
    return mult(combo.get('mult', -1))


@app.route("/division")
@login_required
def division():
    """ The division operation mode """
    return divd(combo.get('divd', -1))


@app.route("/evaluate", methods=["POST"])
@login_required
def evaluate():
    """Evaluates the submitted problem and redirects to the page that the user was in

    Returns:
        [Text]: [The mode that the user is currently visiting]
    """
    
    # getting the answer from the user
    answer = int(request.form.get('answer'))
    # and the operation that they are currently making
    operation = request.form.get('operation')
    
    # the actual answer and the route that this funtion should redirect to
    actual_answer, route = compare.pop()
    print(actual_answer, route)

    if answer == actual_answer:
        
        # additional logic for the division operation
        if operation == "divd":
            remainder = int(request.form.get('remainder'))
            if remainder == actual_answer.pop():
                combo[operation] = combo.get(operation, 0) + 1
            else:
                combo[operation] = 0
        else:
            combo[operation] = combo.get(operation, 0) + 1
            
    else:
        combo[operation] = 0
    
    # for debug    
    print(combo.get(operation))
        
    return redirect(route)
        
        
# EXAM MODE

@app.route("/exam")
@login_required
def exam():
    """
    
    Generates the exam page
    It provides the page with 12 questions, 3 for each operation, 
    and for each question with information like the numbers, the operator, 
    the actual answer and the color of the question. For division remainder 
    is the additional information.

    Returns:
        [Text]: [Exam page in HTML5]
    """
    
     
    # user clicked on a button to do the exam
    
    questions_info = []
    
    # addition
    for _ in range(3):
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        questions_info.append((len(questions_info), {
            "nums": (num1, num2),
            "answer": num1 + num2,
            "operator": '+',
            "color": 'aquamarine',
        }))
        
    # subtraction
    for _ in range(3):
        num2 = randint(0, 100)
        num1 = randint(num2, 100)
        questions_info.append((len(questions_info), {
            "nums": (num1, num2),
            "answer": num1 - num2,
            "operator": '-',
            "color": 'yellow',
        }))
       
    # multiplication 
    for _ in range(3):
        num1 = randint(0, 50)
        num2 = randint(0, 20)
        questions_info.append((len(questions_info), {
            "nums": (num1, num2),
            "answer": num1 * num2,
            "operator": '×',
            "color": 'red',
        }))
        
    # division
    for _ in range(3):
        num1 = randint(0, 100)
        num2 = randint(1, 15)
        questions_info.append((len(questions_info), {
            "nums": (num1, num2),
            "answer": num1 // num2,
            "remainder": num1 % num2,
            "operator": '÷',
            "color": 'mediumpurple',
        }))
       
    # for debug 
    print(questions_info)
    
    return render_template("exam.html", infos=questions_info)

