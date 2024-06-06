from api.models.todos import Todo
from api.utils.get_db import get_db
from api.schemas.todos import TodoCreate, TodoUpdate

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

todo_router = APIRouter(prefix="/todos", tags=["Todo"])

@todo_router.post("/")
def create_todo(todo_data: TodoCreate, db: Session = Depends(get_db)):
    if todo_data.title is None or todo_data.description is None:
        raise HTTPException(status_code=400, detail="Title and description are required")

    new_todo = Todo(title=todo_data.title, description=todo_data.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@todo_router.get("/")
def all_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

@todo_router.get("/{key}")
def post_todo(key: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == key).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@todo_router.put("/{key}")
def update_todo(key: int, todo_data: TodoUpdate, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == key).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    for field, value in todo_data.items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)
    return todo

@todo_router.delete("/{key}")
def delete_todo(key: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == key).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
