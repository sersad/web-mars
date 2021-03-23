from data import db_session
from data.jobs import Jobs
from data.users import User


def add_user():
    """
    Модель Марсиане
    Добавляем капитана
    """
    db_sess = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    db_sess.add(user)

    user = User()
    user.surname = "Weir"
    user.name = "Andy"
    user.age = 18
    user.position = "chief scientist"
    user.speciality = "geologist"
    user.address = "module_1"
    user.email = "andy_chief@mars.org"
    user.hashed_password = "sci"
    user.set_password(user.hashed_password)
    db_sess.add(user)

    user = User()
    user.surname = "Watny"
    user.name = "Mark"
    user.age = 25
    user.position = "middle scientist"
    user.speciality = "biologist"
    user.address = "module_2"
    user.email = "mark@mars.org"
    user.hashed_password = "bio"
    user.set_password(user.hashed_password)
    db_sess.add(user)

    user = User()
    user.surname = "Kapoor"
    user.name = "Venkat"
    user.age = 15
    user.position = "pilot"
    user.speciality = "pilot, navigator"
    user.address = "module_2"
    user.email = "kapoor@mars.org"
    user.hashed_password = "pilot"
    user.set_password(user.hashed_password)
    db_sess.add(user)

    user = User()
    user.surname = "Sanders"
    user.name = "Teddy"
    user.age = 27
    user.position = "programmer"
    user.speciality = "IT specialist"
    user.address = "module_2"
    user.email = "sanders@mars.org"
    user.hashed_password = "comp"
    user.set_password(user.hashed_password)
    db_sess.add(user)

    user = User()
    user.surname = "Bean"
    user.name = "Sean"
    user.age = 17
    user.position = "chief engineer"
    user.speciality = "builder"
    user.address = "module_1"
    user.email = "bean@mars.org"
    user.hashed_password = "build"
    user.set_password(user.hashed_password)
    db_sess.add(user)
    db_sess.commit()


def add_jobs():
    """
    Модель Работы
    Первая работа
    """
    db_sess = db_session.create_session()
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    db_sess.add(job)

    job = Jobs()
    job.team_leader = 1
    job.job = 'exploration of mineral resources'
    job.work_size = 15
    job.collaborators = '4, 3, 6'
    job.is_finished = True

    db_sess.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'development of a management system'
    job.work_size = 25
    job.collaborators = '5'
    job.is_finished = False

    db_sess.add(job)

    job = Jobs()
    job.team_leader = 1
    job.job = 'analysis of atmospheric air samples'
    job.work_size = 15
    job.collaborators = '4, 5'
    job.is_finished = False

    db_sess.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'Mars Rover maintenance'
    job.work_size = 5
    job.collaborators = '4'
    job.is_finished = True

    db_sess.add(job)

    job = Jobs()
    job.team_leader = 1
    job.job = 'preventive vaccinations of the crew'
    job.work_size = 7
    job.collaborators = '3'
    job.is_finished = False

    db_sess.add(job)

    db_sess.commit()
