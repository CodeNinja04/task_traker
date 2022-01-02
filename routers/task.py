from typing import List
from fastapi import APIRouter, Depends
from schemas import TaskBase, TaskDisplay,UserBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_task
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/tasks',
    tags=['task']
)

@router.post('/',response_model=TaskDisplay)
def create_Task(request: TaskBase, db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_task.create_Task(db,request)

@router.get('/{id}')#,response_model=TaskDisplay)
def get_Task(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data':db_task.get_Task(db,id),
        'current_user':current_user
    }
    
