import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    x0 = Column(String(250), nullable=False)
    img = Column(String(250), nullable=False)
    iterations = Column(Integer)
    answers = Column(String(250), nullable=False)
    sets = Column(Integer)


engine = create_engine('sqlite:///main.db')

Base.metadata.create_all(engine)
