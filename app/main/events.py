from flask import session
from flask_socketio import emit, join_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a group.
    A status message is broadcast to all people in the group."""
    group = session.get('group')
    join_room(group)
    emit('status', {'msg': session.get('name') + ' has entered the group.'}, group=group)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the group."""
    group = session.get('group')
    emit('message', {'msg': session.get('name') + ': ' + message['msg']}, group=group)
