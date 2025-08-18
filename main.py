from flask import Flask, render_template, request, redirect
from routes.auth import auth_bp
app = Flask(__name__)
app.config["SECRET_KEY"] = "ahsdjkhasdas"


# Blueprint for auth
app.register_blueprint(auth_bp)


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
