from flask import Blueprint, render_template, request , redirect, url_for, session, jsonify , flash
from flask_login import login_user, logout_user, login_required
from app import db
from app.models.user import User

auth_bp = Blueprint("auth", __name__)

# Register
@auth_bp.route("/register", methods= ["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        password = request.form["password"]

        # Checking if there already have user
        existing_user =  User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        if existing_user:
            flash("User or email already exist !", "error")
            return redirect(url_for("auth.register"))

        # POST method
        new_user = User(
            username=username,
            email=email,
            first_name = first_name,
            last_name = last_name,

        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Create account successfully !","success")
        return redirect(url_for("auth.login"))   

    return render_template("register.html")

# Login
@auth_bp.route("/login", methods= ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash("Wrong user or password !", "error")
            return redirect(url_for("auth.login"))
        
        login_user(user)
        flash("Log in success !", "success")
        return redirect(url_for("home"))
    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Log out success!", "info")
    return redirect(url_for("home"))
