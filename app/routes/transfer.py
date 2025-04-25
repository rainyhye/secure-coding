from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.models import db, User, Transaction
from app.forms.forms import TransferForm

transfer_bp = Blueprint('transfer', __name__)

@transfer_bp.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('auth.login'))

    form = TransferForm()
    sender = User.query.get(session['user_id'])

    if form.validate_on_submit():
        receiver = User.query.filter_by(username=form.receiver_username.data).first()
        amount = form.amount.data

        if not receiver:
            flash('받는 사용자를 찾을 수 없습니다.', 'danger')
            return redirect(url_for('transfer.transfer'))

        if sender.balance < amount:
            flash('잔액이 부족합니다.', 'danger')
            return redirect(url_for('transfer.transfer'))

        # 송금 처리
        sender.balance -= amount
        receiver.balance += amount
        transaction = Transaction(sender_id=sender.id, receiver_id=receiver.id, product_id=None, amount=amount, status='completed')

        db.session.add(transaction)
        db.session.commit()

        flash(f"{receiver.username}님에게 {amount}원을 송금했습니다.", 'success')
        return redirect(url_for('dashboard.user_dashboard'))

    return render_template('transfer.html', form=form)
