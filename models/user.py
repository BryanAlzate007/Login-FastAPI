from config.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    
    __tablename__= "user"
    
    
    id = Column(Integer, primary_key= True, autoincrement="auto")
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String)
    country = Column(String)
    password = Column(String)