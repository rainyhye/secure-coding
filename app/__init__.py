from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_socketio import SocketIO

# 확장기능 인스턴스 생성
db = SQLAlchemy()
csrf = CSRFProtect()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///secure.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 확장기능 등록
    db.init_app(app)
    csrf.init_app(app)
    socketio.init_app(app)

    # 라우터 등록
    from app.routes.auth import auth_bp
    from app.routes.product import product_bp
    from app.routes.chat import chat_bp
    from app.routes.admin import admin_bp
    from app.routes.index import index_bp
    from app.routes.dashboard import user_bp
    from app.routes.profile import profile_bp
    from app.routes.report import report_bp
    from app.sockets import chat_socket
    from app.routes.transfer import transfer_bp
    from app.routes.recharge import recharge_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(user_bp)   
    app.register_blueprint(profile_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(transfer_bp)
    app.register_blueprint(recharge_bp)

    return app


