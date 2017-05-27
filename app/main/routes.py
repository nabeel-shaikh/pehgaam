from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a group."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['group'] = form.group.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.group.data = session.get('group', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat group. The user's name and group must be stored in
    the session."""
    name = session.get('name', '')
    group = session.get('group', '')
    if name == '' or group == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, group=group)
