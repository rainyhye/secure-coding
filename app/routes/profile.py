# app/routes/profile.py
from app import db
from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models.models import User
from app.forms.forms import ProfileForm

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    user = User.query.get(session['user_id'])
    form = ProfileForm()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.commit()
        flash('프로필이 업데이트되었습니다.', 'success')
        return redirect(url_for('profile.profile'))

    form.bio.data = user.bio  # 기존 값 표시
    return render_template('profile.html', user=user, form=form)