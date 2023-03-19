from flask import Flask, render_template

from data import db_session
from data.db_session import create_session
from data.jobs import Jobs
from data.users import User
from data.departaments import Departament

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def catalog_of_jobs():
    db_sess = create_session()
    data = db_sess.query(Jobs).all()
    return render_template('catalog_of_jobs.html', data=data)


def main():
    db_session.global_init('db/blogs.db')


if __name__ == '__main__':
    main()
