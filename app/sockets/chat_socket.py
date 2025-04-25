from flask_socketio import emit
from app import socketio

@socketio.on('send_message')
def handle_message(data):
    username = data.get('username', '익명')
    message = data.get('message', '')
    emit('receive_message', {'msg': message, 'username': username}, broadcast=True)
