from flask import Flask

from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_astro():
    db_sess = db_session.create_session()
    data = [['Scott, Ridley, 21, captain, research engineer, module_1, scott_chief@mars.org'],
            ['Dwayne, Johnson, 24, member, pilot, module_2, johnson_@mars.org'],
            ['Arthur, Hamilton, 28, member, engineer, module_3, Hamilton_@mars.org']]
    for i in data:
        i = i[0].split(', ')
        user = User()
        user.surname = i[0]
        user.name = i[1]
        user.age = int(i[2])
        user.position = i[3]
        user.speciality = i[4]
        user.address = i[5]
        user.email = i[-1]
        db_sess.add(user)
        db_sess.commit()


def main():
    db_session.global_init('db/blogs.db')
    add_astro()
    # app.run()


if __name__ == '__main__':
    main()
