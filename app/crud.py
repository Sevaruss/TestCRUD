from models.test_tab import TestTabSchema
from models.db_utl import test_table, database

async def post(payload: TestTabSchema):
    query = test_table.insert().values(name=payload.name, descr=payload.descr)
    return await database.execute(query=query)

async def get(id: int):
    query = test_table.select().where(id == test_table.c.id)
    return await database.fetch_one(query=query)

async def get_all():
    query = test_table.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: TestTabSchema):
    query = (test_table.update()
             .where(id==test_table.c.id)
             .values(name=payload.name, descr=payload.descr)
             .returning(test_table.c.id))
    return await database.execute(query=query)

async def delete(id: int):
    query = test_table.delete().where(id==test_table.c.id)
    return await database.execute(query=query)

