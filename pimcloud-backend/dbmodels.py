from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    calendars = relationship("Calendar", back_populates="user")


class Calendar(Base):
    __tablename__ = 'calendars'

    calendar_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    url = Column(String, unique=True, nullable=False)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="calendars")
    tasks = relationship("Task", back_populates="calendar")


class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True, index=True)
    calendar_id = Column(Integer, ForeignKey('calendars.calendar_id'), nullable=False)
    uid = Column(String, unique=True, nullable=False)
    summary = Column(String, nullable=False)
    due_date = Column(DateTime)
    status = Column(String, default='Pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    calendar = relationship("Calendar", back_populates="tasks")