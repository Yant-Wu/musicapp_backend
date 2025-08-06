from models.base import Base
from sqlalchemy import LargeBinary,VARCHAR,Text,Column

class User(Base):
    __tablename__ = 'users'
    id = Column(Text,primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)