import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, nullable=False)
    x0 = Column(String(250), nullable=False)
    img = Column(String(250), nullable=False)
    iterations = Column(Integer, nullable=False)
    answers = Column(String(250), nullable=False)
    sets = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    result = Column(Integer, nullable=False)
    result_procent = Column(Integer, nullable=False)


engine = create_engine('sqlite:///main.db')

Base.metadata.create_all(engine)
