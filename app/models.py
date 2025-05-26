from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    quote = Column(String, nullable=False)
    image = Column(String, nullable=True)
    likes = Column(Integer, default=0)
