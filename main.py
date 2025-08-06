from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import LargeBinary,VARCHAR,Text,Column,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
import bcrypt 

app = FastAPI()

DATABASE_URL = 'postgresql://postgres:postgres@localhost:8700/musicapp'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Text,primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)

@app.post("/signup")
def signup_user(user: UserCreate):
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400,'User with the same email already exists')

    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt(16))
    user_db = User(id=str(uuid4()), name=user.name, email=user.email, password=hashed_password)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db

Base.metadata.create_all(engine)