from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astro = StringField('id астронавта', validators=[DataRequired()])
    password_astro = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username = StringField('id капитана', validators=[DataRequired()])
    password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')