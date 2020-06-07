import datetime

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from api.data.db_session import SqlAlchemyBase


class Item(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'items'
    id = sqlalchemy.column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    estimate_id = sqlalchemy.column(sqlalchemy.Integer, sqlalchemy.ForeignKey("estimates.id"), nullable=False)
    name = sqlalchemy.column(sqlalchemy.String, nullable=False)
    quantity = sqlalchemy.column(sqlalchemy.String, nullable=False)
    reg_date = sqlalchemy.column(sqlalchemy.DateTime, default=datetime.datetime.now())
    area = sqlalchemy.column(sqlalchemy.String)
    status = sqlalchemy.column(sqlalchemy.Integer, default=0)

    estimate = orm.relation("Estimate", foreign_keys=[estimate_id])
