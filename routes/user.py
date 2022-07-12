from fastapi import APIRouter, FastAPI
from config.db import connect
from models.index import users
from schemas.index import User
user = APIRouter()

@user.get("/")
async def read_data():
    return connect.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id: int):
    return connect.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def write_data(user: User):
    connect.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    return connect.execute(users.select()).fetchall()


@user.put("/{id}")
async def update_data(id:int, user: User):
    connect.execute(users.update(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    return connect.execute(users.select()).fetchall()

@user.delete("/{id}")
async def delete_data(id: int):
    connect.execute(users.delete().where(users.c.id == id))
    return connect.execute(users.select()).fetchall()