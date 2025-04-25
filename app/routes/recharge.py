from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.models.models import db, User
from app.forms.forms import RechargeForm

recharge_bp = Blueprint('recharge', __name__)

@recharge_bp.route('/recharge', methods=['GET', 'POST'])
def recharge():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('auth.login'))

    user = User.query.get(session['user_id'])
    form = RechargeForm()

    if form.validate_on_submit():
        amount = form.amount.data
        user.balance += amount
        db.session.commit()
        flash(f'{amount}원 충전 완료!', 'success')
        return redirect(url_for('dashboard.user_dashboard'))

    return render_template('recharge.html', form=form)
