from fastapi import APIRouter

todo_router = APIRouter(prefix="/todos", tags=["Todo"])

@todo_router.post("/")
def create_todo():
    return "Not Implemented"

@todo_router.get("/")
def all_todos():
    return "Not Implemented"

@todo_router.get("/{key}")
def post_todo(key: int):
    return "Not Implemented"

@todo_router.put("/{key}")
def update_todo(key: int):
    return "Not Implemented"

@todo_router.delete("/{key}")
def delete_todo(key: int):
    return "Not Implemented"
