import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)  # фамилия
    name = sqlalchemy.Column(sqlalchemy.String)  # имя
    age = sqlalchemy.Column(sqlalchemy.Integer)  # возраст
    position = sqlalchemy.Column(sqlalchemy.String)  # должность
    speciality = sqlalchemy.Column(sqlalchemy.String)  # профессия
    address = sqlalchemy.Column(sqlalchemy.String)  # адрес
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)  # электронная почта
    hashed_password = sqlalchemy.Column(sqlalchemy.String)  # хэшированный пароль
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now())  # дата изменения

    jobs = orm.relation("Jobs", back_populates='user')

    def __repr__(self):
        return f"<User> <Colonist> {self.id} {self.surname} {self.name}"

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)