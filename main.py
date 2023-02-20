from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = 'g'


class LoginForm(FlaskForm):
    id_astro = StringField('', validators=[DataRequired()])
    password_astro = PasswordField('', validators=[DataRequired()])
    id_captain = StringField('', validators=[DataRequired()])
    password_captain = PasswordField('', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return
    return render_template("double_protection.html", form=form, title='Авторизация')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
