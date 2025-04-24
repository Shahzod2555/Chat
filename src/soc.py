from flask_login import current_user
from flask_socketio import join_room, emit
from model import Message, User
from ext import db


def handle_connect():
    if current_user.is_authenticated:
        join_room(str(current_user.id))
        emit('after_connect', {'data': 'Соединение установлено.'})
    else:
        emit('after_connect', {'data': 'Ошибка подключения: пользователь не авторизован.'})


def handle_send_private_message_event(data):
    if not current_user.is_authenticated:
        return emit('error', {'data': 'Авторизуйтесь для отправки сообщений.'})

    recipient_id = data.get('recipient_id')
    message_text = data.get('message', '').strip()

    if not recipient_id or not message_text:
        return emit('error', {'data': 'Некорректные данные.'})

    recipient = User.query.get(recipient_id)
    if not recipient:
        return emit('error', {'data': f"Пользователь с ID {recipient_id} не найден."})

    try:
        message = Message(sender_id=current_user.id, recipient_id=recipient_id, content=message_text)
        db.session.add(message)
        db.session.commit()

        emit('receive_private_message', {
            'sender_id': current_user.id,
            'sender_name': current_user.username,
            'message': message_text
        }, room=str(recipient_id))

        emit('receive_private_message', {
            'sender_id': current_user.id,
            'sender_name': current_user.username,
            'message': message_text
        }, room=str(current_user.id))

    except Exception as e:
        db.session.rollback()
        emit('error', {'data': f'Ошибка сохранения: {str(e)}'})
