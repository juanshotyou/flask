from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.route("/")
def index():
    admin = {"username": "Vlad"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="Home", user=admin, posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)

@app.route("/firepower")
def firepower():
    return render_template("index.html", title="Firepower")

@app.route("/webex")
def webex():
    return render_template("index.html", title="Webex")

@app.route("/meraki")
def meraki():
    return render_template("index.html", title="Meraki")