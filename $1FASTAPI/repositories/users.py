from typing import Optional
from .base import BaseRepository
import datetime
from db.users import users
from core.security import hash_password
from models.users import User, UserRegister


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0):
        query = users.select().limit(limit).offset(skip)
        result = await self.database.fetch_all(query=query)
        return result

    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserRegister) -> User:
        user = User(
            name=u.name,
            email=u.email.lower(),
            hashed_password=hash_password(u.password),
            created_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id", None)

        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email == email.lower())
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def update_name(self, current_user: User, id: int, new_name: str):
        query = users.update().where(users.c.id == id).values(name=new_name)
        await self.database.execute(query)
        return f"Name was changed successfully: from \'{current_user.name}\' to \'{new_name}\'."

    async def update_password(self, id: int, new_password: str,password_accepted: str):
        if password_accepted != new_password:
            return {"error": "Passwords does not match", "status": False, "payload": []}
        query = users.update().where(users.c.id == id).values(hashed_password=hash_password(new_password))
        await self.database.execute(query)
        return f"Password was changed successfully"

