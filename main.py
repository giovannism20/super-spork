from fastapi import FastAPI
from api.routes.todo import todo_router

app = FastAPI()
app.include_router(todo_router)
