from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """Accepts a nickname and a group."""
    name = StringField(
        'Name',
        validators=[DataRequired()],
        render_kw={
            'placeholder': 'Your Name',
            'required': True},
    )
    group = StringField(
        'group',
        validators=[DataRequired()],
        render_kw={
            'placeholder': 'Group',
            'required': True},
    )
    submit = SubmitField('Send')
