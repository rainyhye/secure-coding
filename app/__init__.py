# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# 확장기능 인스턴스 생성 (초기화는 아래 create_app에서)
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///secure.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 확장기능 앱에 등록
    db.init_app(app)
    csrf.init_app(app)

    # 라우터 등록
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    # 필요한 경우 여기에 더 등록 가능:
    # from app.routes.product import product_bp
    # app.register_blueprint(product_bp)

    return app

