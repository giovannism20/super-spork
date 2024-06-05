from fastapi import FastAPI
from api.routes.todos import todo_router

app = FastAPI()
app.include_router(todo_router)
