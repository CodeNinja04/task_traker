from typing import List
from pydantic import BaseModel


class Task(BaseModel):
    title: str
    content: str
    status:int 

    class Config():
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDispaly(BaseModel):
    username: str
    email: str
    items: List[Task] = []

    class Config():
        orm_mode = True


class User(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class TaskBase(BaseModel):
    title: str
    content: str
    status: int
    creator_id: int


class TaskDisplay(BaseModel):
    title: str
    content: str
    status: int
    user: User

    class Config():
        orm_mode = True
