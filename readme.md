# Secure Coding Project - 중고거래 플랫폼

이 프로젝트는 Flask 기반으로 구축된 중고거래 웹 플랫폼입니다.  
사용자는 상품을 등록하고, 송금 및 충전 기능을 사용할 수 있으며, 실시간 채팅으로 소통할 수 있습니다.

---

## 🛠️ 설치 및 실행 방법

### 1. 프로젝트 클론

bash
git clone https://github.com/사용자명/secure-coding.git
cd secure-coding 2. 가상환경 생성 및 활성화

# 가상환경 생성

python -m venv venv

# Windows

venv\Scripts\activate

# Mac/Linux

source venv/bin/activate

3. 필요한 패키지 설치
   pip install -r requirements.txt

4. 데이터베이스 생성

# Python 쉘 진입

python

# DB 생성

from app import db, create_app
app = create_app()
with app.app_context():
db.create_all()
exit()

5. 서버 실행
   python run.py

관리자 계정 생성 방법

[app.py](http://app.py) 있는 루트 디렉토리에서

scripts/\_init_admin.py 만듬

→ 버전 호환 안될 시

pip install "werkzeug<3.0"
