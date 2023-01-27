import sqlalchemy
from .base import metadata
import datetime



models = sqlalchemy.Table(
                'models',
                metadata,
                sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
                sqlalchemy.Column("title", sqlalchemy.String),
                sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
                sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
                )
