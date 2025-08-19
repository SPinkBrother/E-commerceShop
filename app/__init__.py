from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Config viết trực tiếp
    app.config['SECRET_KEY'] = 'asdkjaklsdjkasjd'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:131120@localhost:5432/shein_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Khởi tạo extension
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Import blueprint
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
