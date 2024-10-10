from fastapi import FastAPI
from models import find, findAll

app = FastAPI()


@app.get("/logs")
async def getAllLogs():
    return findAll()


@app.get("/logs/{user_id}")
async def getLogs(user_id: int):
    return find(user_id)
