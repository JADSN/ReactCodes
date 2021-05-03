from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date

from database import Base


# class UserItem(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True,
#                 autoincrement=True,  unique=True, index=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     password = Column(String, unique=False, index=True, nullable=False)


class TaskIem(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True,
                autoincrement=True,  unique=True, index=True)
    text = Column(String, unique=False, index=True, nullable=False)
    day = Column(String, nullable=False)
    reminder = Column(Boolean, nullable=False)

    # items = relationship("Item", back_populates="owner")
