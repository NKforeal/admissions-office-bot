from sqlalchemy import update

from DAO.base import BaseDAO
from db.database import async_session_maker
from db.models.users import Users


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def update_by_tg_id(cls, tg_id, **data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.tg_id==tg_id).values(**data)
            await session.execute(query)
            await session.commit()