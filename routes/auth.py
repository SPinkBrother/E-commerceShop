from flask import Blueprint, render_template, request , redirect, url_for, session, jsonify , flash

auth_bp = Blueprint("auth", __name__)

# DB testing
users = {}


# Register
@auth_bp.route("/register", methods= ["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            flash("User already exists !", "error")
        users[username] = password

        flash("Log in success !", "success")
        return redirect(url_for("auth.login"))
    

    return render_template("register.html")

# Login
@auth_bp.route("/login", methods= ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username != "admin" or password != "123":
            flash("Wrong user or password !", "error")
            return redirect(url_for("login"))

        flash("Log in success !", "success")
        return redirect(url_for("home"))
    return render_template("login.html")

