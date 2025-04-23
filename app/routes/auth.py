from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.models import db, User
from app.forms.forms import LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # 중복 사용자 확인
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('이미 존재하는 사용자입니다.', 'error')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Complete Register! Please login', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash('Success login!', 'success')
            return redirect(url_for('dashboard')) #나중에 별도 구현
        else:
            flash('Wrong id or password.', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('logout.', 'success')
    return redirect(url_for('auth.login'))