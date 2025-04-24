from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.models.models import db, User, Message

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat/<int:user_id>', methods=['GET', 'POST'])
def chat(user_id):
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        message = request.form['message']
        new_msg = Message(
            sender_id=session['user_id'],
            receiver_id=user_id,
            message=message
        )
        db.session.add(new_msg)
        db.session.commit()
        return redirect(url_for('chat.chat', user_id=user_id))

    messages = Message.query.filter(
        ((Message.sender_id == session['user_id']) & (Message.receiver_id == user_id)) |
        ((Message.sender_id == user_id) & (Message.receiver_id == session['user_id']))
    ).order_by(Message.timestamp.asc()).all()

    receiver = User.query.get_or_404(user_id)
    return render_template('chat/chat.html', messages=messages, receiver=receiver)