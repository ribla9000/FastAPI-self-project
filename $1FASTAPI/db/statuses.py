import sqlalchemy
from .base import metadata


statuses = sqlalchemy.Table(
                'statuses',
                metadata,
                sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
                sqlalchemy.Column("status_name", sqlalchemy.String),
                sqlalchemy.Column("bool", sqlalchemy.Boolean, default=True),
                )