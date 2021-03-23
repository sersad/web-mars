import datetime

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))  # (id) (id руководителя, целое число)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # (description) (описание работы)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, default=0)  # (hours) (объем работы в часах)
    collaborators = sqlalchemy.Column(sqlalchemy.String)  # (list of id of participants) (список id участников)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)  # (дата начала)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)  # (bool) (признак завершения)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)  #

    user = orm.relation('User', back_populates='jobs')

    def __repr__(self):
        return f"<Jobs> {self.id}-{self.team_leader}- {self.job}-{self.work_size}"
