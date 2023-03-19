import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class Departament(SqlAlchemyBase):
    __tablename__ = 'departaments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    members = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True, unique=True)
    user = orm.relationship("User")
