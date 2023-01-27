from .statuses import statuses
from .models import models
from .users import users
from .base import metadata, engine


metadata.create_all(bind=engine)