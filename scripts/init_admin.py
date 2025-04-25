# scripts/init_admin.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app, db
from app.models.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # 이미 관리자 존재하는지 확인
    existing_admin = User.query.filter_by(username='admin').first()
    if existing_admin:
        print("이미 admin 계정이 존재합니다.")
    else:
        admin = User(
            username='admin',
            email='admin@site.com',
            password_hash=generate_password_hash('admin1234'),
            role='admin',
            status='active'
        )
        db.session.add(admin)
        db.session.commit()
        print("관리자 계정 생성 완료: admin / admin1234")
