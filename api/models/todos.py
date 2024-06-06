from sqlalchemy import Column, Integer, String
from api.database.database import Base

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)

    def __repr__(self):
        return f"({self.id} {self.title} {self.description})"
