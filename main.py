from flask import Flask, render_template, request, redirect
from app import create_app

app = create_app()



# Home route
@app.route("/")
def home():
    return render_template("home.html")
# Cart route
@app.route("/mycart")
def mycart():
    return render_template("user_cart.html")

if __name__ == "__main__":
    app.run(debug=True)
