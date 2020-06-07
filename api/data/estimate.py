import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from api.data.db_session import SqlAlchemyBase


class Estimate(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'estimates'
    id = sqlalchemy.column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.column(sqlalchemy.String, nullable=False)
    user_id = sqlalchemy.column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False)

    items = orm.relation("Item", back_populates="estimate", cascade="all, delete, delete-orphan")
    user = orm.relation("User", foreign_keys=[user_id])
