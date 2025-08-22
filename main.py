from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from app import create_app,db

app = create_app()
migrate = Migrate(app, db)



# Home route
@app.route("/")
def home():
    return render_template("home.html")

# User profile route
@app.route("/<int:user_id>_profile")
def profile(user_id):
    return render_template("profile.html",user_id= user_id)

# Cart route
@app.route("/mycart")
def mycart():
    return render_template("user_cart.html")

if __name__ == "__main__":
    app.run(debug=True)
