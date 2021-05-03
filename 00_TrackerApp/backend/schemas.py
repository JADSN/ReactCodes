from pydantic import BaseModel
from typing import Optional, List

# TASK


class TaskIem(BaseModel):
    id: int = 1
    text: str
    day: str
    reminder: bool


class CreateTaskIem(BaseModel):
    text: str
    day: str


class UpdateTaskIem(BaseModel):
    reminder: bool

# USER


# class UserItem(BaseModel):
#     id: int = 1
#     email: str
#     password: str


# class UserAuth(BaseModel):
#     password: str


# class CreateUserItem(BaseModel):
#     email: str
#     password: str
