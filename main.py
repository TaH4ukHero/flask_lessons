from flask import Flask, redirect, render_template, jsonify
from flask_login import LoginManager, login_user

from data import db_session
from data.add_forms import AddJobForm
from data.db_session import create_session
from data.jobs import Jobs
from data.login_form import LoginForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/add_job', methods=["GET", "POST"])
def add_job():
    add_form = AddJobForm()
    if add_form.validate_on_submit():
        db_sess = create_session()
        jobs = Jobs(job=add_form.job.data,
                    team_leader=add_form.team_leader.data,
                    work_size=add_form.work_size.data,
                    collaborators=add_form.collaborators.data,
                    is_finished=add_form.is_finished.data)
        db_sess.add(jobs)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/api/jobs/<int:job_id>')
def get_news(job_id: int):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(job_id)
    if not str(job_id).isdigit():
        return jsonify(
            {
                "error": "Not Found"
            }
        )
    return jsonify(
        {
            "title": news.to_dict(only='title')
        }
    )


if __name__ == '__main__':
    db_session.global_init('db/blogs.db')

    app.run()
