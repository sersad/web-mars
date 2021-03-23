from pprint import pprint

from flask import Flask, render_template, make_response, jsonify
from flask_login import LoginManager

from add_data_db import add_user, add_jobs
from data import db_session, jobs_api
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    """
    Журнал работ
    :return:
    """
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    params = {'title': 'Миссия на МАРС',
              'jobs': jobs}
    return render_template('index.html', **params)


@app.errorhandler(404)
def not_found(error):
    """при передаче неправильного параметра ответ от сервера будет приходить в формате JSON,
    и клиентское приложение не будет падать
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    # Добавляем капитана
    # add_user()
    #
    # # Первая работа
    # add_jobs()

    # # Запрос 1
    # выводит всех колонистов, проживающих в первом модуле, каждого с новой строки.
    # users = db_sess.query(User).filter(User.address == 'module_1')
    # for user in users:
    #     print(user)

    # # Запрос 2
    # выводит id колонистов, которые проживают в 1 модуле и ни профессия (speciality), ни должность (position)
    # которых не содержат подстроку engineer, каждый с новой строки.
    # users = db_sess.query(User).filter(User.address == 'module_1', User.speciality.notlike('%engineer%'),
    #                                    User.position.notlike('%engineer%'))
    # for user in users:
    #     print(user.id, user.position, user.speciality, user.address)

    # Запрос 3
    #  выводит всех несовершеннолетних (возраст меньше 18) колонистов
    #  с указанием возраста в годах, каждого с новой строки.
    # users = db_sess.query(User).filter(User.age < 18)
    # for user in users:
    #     print(user, user.age, "years")

    # # Запрос 4
    # выводит колонистов, у которых в названии должности есть
    # chief или middle, каждого с новой строки.
    # users = db_sess.query(User).filter(User.position.like('%chief%') |
    #                                    User.position.like('%middle%'))
    # for user in users:
    #     print(user, user.position)

    # Запрос 5
    # выводит работы, выполнение которых требует меньше 20 часов и которые еще
    # не закончены, каждую с новой строки.
    # jobs = db_sess.query(Jobs).filter(Jobs.work_size < 20,
    #                                   Jobs.is_finished == 0)
    # for job in jobs:
    #     print(job)

    # # Запрос 6
    # ыводит фамилии и имена тимлидов тех работ, которые выполняются наибольшими
    # командами. Если наибольшая команда одна, то одного тимлида, если команд
    # с наибольшим размером несколько, то всех.
    # jobs = db_sess.query(Jobs).filter(Jobs.collaborators)
    # collaborators = {job.id: list(map(int, job.collaborators.split(", ")))
    #                  for job in jobs}
    # max_jobs = list(filter(lambda x: len(x[1]) >= len(max(collaborators.values(), key=len)),
    #                   collaborators.items()))
    # ids = [x[0] for x in max_jobs]
    # jobs = db_sess.query(Jobs).filter(Jobs.id.in_(ids)).all()
    # for job in jobs:
    #     print(job)

    # Запрос 7
    # и изменяет всем, проживающим в модуле 1 и имеющим возраст менее 21 года,
    # адрес на module_3.

    # app.register_blueprint(jobs_api.blueprint)

    # jobs = db_sess.query(Jobs).all()
    # for job in jobs:
    #     print(job.job)

    # jobs = db_sess.query(Jobs).get(1)
    # user = db_sess.query(User).get(1)
    #
    # print(jobs.user)
    # print(user.jobs)

    # jobs = db_sess.query(Jobs).all()
    # for job in jobs:
    #     print(job.user.name, job.user.surname)

    app.run(port="8080", host="127.0.0.1")


if __name__ == '__main__':
    main()
