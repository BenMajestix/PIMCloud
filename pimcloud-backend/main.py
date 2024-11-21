from fastapi import FastAPI
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .db import Base, engine, SessionLocal
from .dbmodels import User, Calendars, Tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
  
class UserCreate(Basemodel):
  username: str
  password: str

class userAuth(BaseModel):
  username: str
  password: str

# TODO 
# Register & Login Endpoints

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
