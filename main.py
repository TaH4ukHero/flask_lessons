from flask import Flask, render_template
from data import db_session
from data.db_session import create_session, global_init
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def catalog_of_jobs():
    db_sess = create_session()
    data = db_sess.query(Jobs).all()
    return render_template('catalog_of_jobs.html', data=data)

def main():
    # global_init(input())
    db_session.global_init('db/blogs.db')
    app.run()


if __name__ == '__main__':
    main()
