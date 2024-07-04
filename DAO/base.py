from db.database import async_session_maker
from sqlalchemy import select, insert, delete, update


class BaseDAO:
    model = None
    model_id = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)

            return result.mappings().one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filters_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters_by)
            result = await session.execute(query)

            return result.unique().scalars().one_or_none()

    @classmethod
    async def find_all_scalars(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)

            return result.unique().scalars().all()

    @classmethod
    async def find_all_mapping(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)

            return result.unique().mappings().all()

    @classmethod
    async def find_all_offset(cls, offset: int, limit: int, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).offset(offset=offset).limit(limit=limit).filter_by(**filter_by)
            result = await session.execute(query)

            return result.unique().scalars().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, **data):
        async with async_session_maker() as session:
            query = update(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_by_id(cls, data):
        async with async_session_maker() as session:

            query = delete(cls.model).where(cls.model.id == data)
            await session.execute(query)
            await session.commit()
