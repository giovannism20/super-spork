from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///todos.db')

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, autoincrement=True,  nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)

    def __repr__(self):
        return f"({self.id} {self.title} {self.description})"

Base.metadata.create_all(engine)
