import datetime

from flask import Flask, render_template, redirect
from sqlalchemy_lessons.data import db_session
from sqlalchemy_lessons.data.users import User
from sqlalchemy_lessons.data.jobs import Jobs
from sqlalchemy_lessons.forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(input())
    session = create_session()
    for user in session.query(User).filter(User.address == 'module_1',
                                           User.speciality.notlike("%engineer%"),
                                           User.position.notlike("%engineer%")):
        print(user.name)


if __name__ == '__main__':
    main()
