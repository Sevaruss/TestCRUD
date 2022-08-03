from fastapi import FastAPI

from app import test_tab_entry
from models.db_utl import database, engine, metadata

#metadata.create_all(engine)

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"Hello": "world!"}

"""@app.get("/ping")
async def ping():
    query = (select( [test_table.c.id, test_table.c.name]).select_from(test_table))
    return await database.fetch_all(query)
"""

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(test_tab_entry.router, prefix="/test_tab", tags=["test_tab"])
