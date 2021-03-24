import os

from flask import Flask, render_template
from flask_login import LoginManager

from data import db_session, users_resource, jobs_resource
from data.jobs import Jobs
from data.users import User
from flask_restful import Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api = Api(app)
# для списка объектов
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')

# # для одного объекта
api.add_resource(users_resource.UserResource, '/api/v2/users/<int:user_id>')
api.add_resource(jobs_resource.JobResource, '/api/v2/jobs/<int:job_id>')

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


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, host="0.0.0.0")


if __name__ == '__main__':
    main()
