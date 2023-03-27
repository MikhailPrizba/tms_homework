from sqlalchemy import Column, DateTime,  Integer, String

from hw39.db import Base

class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    date_posted = Column(DateTime())
    