import os

# import some of the required items, most are from CS50 finance
from cs50 import SQL
from flask import url_for, Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from os import urandom
import re
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)
app.secret_key = urandom(24)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
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

# Configure CS50 Library to use SQLite database called howareyou.db
db = SQL("sqlite:///howareyou.db")

# this returns the homepage, index.html
@app.route("/")
def index():
    return render_template("index.html")

# this is the yourname page and has two methods, the get which is if you enter the url to get to this page
# and also the post method if you click on the submit button, which stores the information entered into the table
# and then submits it to the howareyou.db
@app.route("/yourname", methods=["GET", "POST"])
def yourname():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
# entered in the text box
        yourname = request.form.get("yourname")
        session["key"] = db.execute("INSERT INTO responses (name) VALUES (:yourname)", yourname=yourname)
        return redirect(url_for("question1"))

    else:
        return render_template("yourname.html")


@app.route("/question1", methods=["GET", "POST"])
def question1():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # use the name of the textbox to insert into the responses table
        question_first = request.form.get("question_first")
        db.execute("UPDATE responses SET question1 = :question_first WHERE name_id = :key",
                   question_first=question_first, key=session["key"])
        # using cookies to save the session

        return redirect("/question2")

    else:
        return render_template("question1.html")


@app.route("/question2", methods=["GET", "POST"])
def question2():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # use the name of the textbox to insert into the responses table
        question_second = request.form.get("question_second")
        db.execute("UPDATE responses SET question2 = :question_second WHERE name_id = :key",
                   question_second=question_second, key=session["key"])

        return redirect("/question3")

    else:
        return render_template("question2.html")


@app.route("/question3", methods=["GET", "POST"])
def question3():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # use the name of the textbox to insert into the responses table
        question_third = request.form.get("question_third")
        db.execute("UPDATE responses SET question3 = :question_third WHERE name_id = :key",
                   question_third=question_third, key=session["key"])

        return redirect("/question4")

    else:
        return render_template("question3.html")


@app.route("/question4", methods=["GET", "POST"])
def question4():

    if request.method == "POST":

        # use the name of the textbox to insert into the responses table
        question_fourth = request.form.get("question_fourth")
        db.execute("UPDATE responses SET question4 = :question_fourth WHERE name_id = :key",
                   question_fourth=question_fourth, key=session["key"])

        return redirect("/question5")

    else:
        return render_template("question4.html")


@app.route("/question5", methods=["GET", "POST"])
def question5():

    if request.method == "POST":

        # use the name of the textbox to insert into the responses table
        question_fifth = request.form.get("question_fifth")
        db.execute("UPDATE responses SET question5 = :question_fifth WHERE name_id = :key",
                   question_fifth=question_fifth, key=session["key"])

        return redirect("/question6")

    else:
        return render_template("question5.html")


@app.route("/question6", methods=["GET", "POST"])
def question6():

    if request.method == "POST":

        # use the name of the textbox to insert into the responses table
        question_sixth = request.form.get("question_sixth")
        db.execute("UPDATE responses SET question6 = :question_sixth WHERE name_id = :key",
                   question_sixth=question_sixth, key=session["key"])

        return redirect("/question7")

    else:
        return render_template("question6.html")


@app.route("/question7", methods=["GET", "POST"])
def question7():

    if request.method == "POST":

        # use the name of the textbox to insert into the responses table
        question_seventh = request.form.get("question_seventh")
        db.execute("UPDATE responses SET question7 = :question_seventh WHERE name_id = :key",
                   question_seventh=question_seventh, key=session["key"])

        return redirect("/recommendation")

    else:
        return render_template("question7.html")


@app.route("/recommendation", methods=["GET", "POST"])
def recommendation():

    if request.method == "POST":

        return redirect("/resources")

    else:

        Contact = False
        ECHO = False
        Indigo = False
        Response = False
        Room13 = False
        ToRecommend = False

        # do this to parse through the words entered in the text box
        # (can only detect one word at a time)
        words1 = db.execute("SELECT question1 FROM responses WHERE name_id = :key", key=session["key"])[0]["question1"]
        words1lower = words1.lower()
        words1splitted = re.split('\W+', words1lower)

        # these are the words that we chose to be "hits", so when these words are entered, then Room13 will become true
        # once Room13 is true, then it will show up as a recommendation and will be on the table as Room 13 in recommendation.html
        for i in words1splitted:
            if (i == "bad" or i == "stress" or i == "stressed" or i == "none" or i == "bad" or i == "sad" or i == "nothing" or i == "deadlines" or i == "midterm" or i == "midterm" or i == "final" or i == "finals"):
                Room13 = True

        words2 = db.execute("SELECT question2 FROM responses WHERE name_id = :key", key=session["key"])[0]["question2"]
        words2lower = words2.lower()
        words2splitted = re.split('\W+', words2lower)

        for i in words2splitted:
            if (i == "stress" or i == "stressed" or i == "none" or i == "no" or i == "bad" or i == "sad" or i == "parents" or i == "family" or i == "exams" or i == "deadlines" or i == "midterm" or i == "midterm" or i == "final" or i == "finals" or i == "lonely" or i == "alone"):
                Room13 = True
            if (i == "identity" or i == "sexuality" or i == "hate" or i == "love"):
                Contact = True
            if (i == "appearance" or i == "eating" or i == "exercise" or i == "body" or i == "image" or i == "fat" or i == "skinny" or i == "skip" or i == "skipping" or i == "little" or i == "inconsistent" or i == "overweight" or i == "underweight" or i == "heavy" or i == "big" or i == "small"):
                ECHO = True

        words3 = db.execute("SELECT question3 FROM responses WHERE name_id = :key", key=session["key"])[0]["question3"]
        words3lower = words3.lower()
        words3splitted = re.split('\W+', words3lower)

        for i in words3splitted:
            if (i == "yes" or i == "less" or i == "tired" or i == "stress" or i == "stressed"):
                Room13 = True
            if (i == "miss" or i == "missing" or i == "homesick" or i == "home-sick" or i == "home"):
                Indigo = True

        words4 = db.execute("SELECT question4 FROM responses WHERE name_id = :key", key=session["key"])[0]["question4"]
        words4lower = words4.lower()
        words4splitted = re.split('\W+', words4lower)

        for i in words4splitted:
            if (i == "room" or i == "little" or i == "inconsistent" or i == "inconsistently" or i == "fat" or i == "skinny" or i == "small" or i == "big" or i == "diet" or i == "dieting" or i == "purge" or i == "purging" or i == "exercise" or i == "body" or i == "image" or i == "skip" or i == "skipping" or i == "much"):
                ECHO = True

        words5 = db.execute("SELECT question5 FROM responses WHERE name_id = :key", key=session["key"])[0]["question5"]
        words5lower = words5.lower()
        words5splitted = re.split('\W+', words5lower)

        for i in words5splitted:
            if (i == "none" or i == "not" or i == "unhappy" or i == "sad" or i == "little"):
                Room13 = True
            if (i == "died" or i == "past" or i == "sick" or i == "ill" or i == "miss" or i == "hospital" or i == "medical" or i == "surgery" or i == "financial" or i == "hardship" or i == "money" or i == "poor"):
                Indigo = True

        words6 = db.execute("SELECT question6 FROM responses WHERE name_id = :key", key=session["key"])[0]["question6"]
        words6lower = words6.lower()
        words6splitted = re.split('\W+', words6lower)

        for i in words6splitted:
            if (i == "none" or i == "breakup" or i == "break" or i == "sad" or i == "broke" or i == "hookup" or i == "broken" or i == "little" or i == "miss" or i == "hate"):
                Response = True
            if (i == "identity" or i == "gay" or i == "queer" or i == "lesbian" or i == "LGBT" or i == "LGBTQ" or i == "LGBTQ+" or i == "BGLTQ+" or i == "BGLTQ"):
                Contact = True

        words7 = db.execute("SELECT question7 FROM responses WHERE name_id = :key", key=session["key"])[0]["question7"]
        words7lower = words7.lower()
        words7splitted = re.split('\W+', words7lower)

        for i in words7splitted:
            if (i == "fail" or i == "failing" or i == "poorly" or i == "academics" or i == "academics" or i == "studies" or i == "studying"):
                Room13 = True
            if (i == "friends" or i == "social" or i == "relationships" or i == "relationship"):
                Response = True
            if (i == "financial" or i == "broke" or i == "miss" or i == "missing"):
                Indigo = True
            if (i == "food" or i == "meals" or i == "bulimia" or i == "bulimic" or i == "anorexia" or i == "anorexic"):
                ECHO = True

        if (Contact == True or ECHO == True or Indigo == True or Response == True or Room13 == True):
            ToRecommend = True

        return render_template("recommendation.html", Contact=Contact, ECHO=ECHO, Indigo=Indigo, Response=Response, Room13=Room13, ToRecommend=ToRecommend)


@app.route("/resources")
def resources():

    return render_template("resources.html")