from flask import Flask, render_template, redirect

from data import db_session
from data.add_forms import AddJobForm
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = AddJobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        data = [form.team_leader.data, form.job.data, form.work_size.data,
                form.collaborators.data, form.is_finished.data]
        user = db_sess.query(User).filter(User.id == data[0]).all()
        if user:
            job.team_leader = data[0]
            job.job = data[1]
            job.work_size = data[2]
            job.collaborators = data[3]
            job.is_finished = data[-1]
            db_sess.add(job)
            db_sess.commit()
            return redirect('/')
        return render_template('add_job.html', form=form, message='Пользователя с таким id не '
                                                                  'существует')
    return render_template('add_job.html', form=form)


def main():
    db_session.global_init('db/blogs.db')
    app.run()


if __name__ == '__main__':
    main()
