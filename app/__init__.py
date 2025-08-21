from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


def load_user(user_id):

    return User.query.get(int(user_id))

# Extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder="../templates")

    # Config viết trực tiếp
    app.config['SECRET_KEY'] = 'asdkjaklsdjkasjd'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:131120@localhost:5432/shein_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Khởi tạo extension
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    bcrypt.init_app(app)

    #Import Models
    from app.models.user import User
    

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    # Import blueprint
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
