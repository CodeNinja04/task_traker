from sqlalchemy.orm import Session
from db.models import DbTask
#from router.exceptions import StoryException
from schemas import TaskBase
from fastapi import HTTPException,status

def create_Task(db:Session,request:TaskBase):
    
    new_task = DbTask(
        title=request.title,
        content=request.content,
        status=request.status,
        end=request.end,
        user_id=request.creator_id
        
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_Task(db:Session,id:int):
    task=db.query(DbTask).filter(DbTask.id==id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    return task
    
def delete_task(id:int, db : Session ):
    task= db.query(DbTask).filter(DbTask.id==id).first()
    db.delete(task)
    db.commit()
    return "task deleted"

def update_task(id : int , db :Session , request: TaskBase):
    task= db.query(DbTask).filter(DbTask.id==id)
    task.update(
        {
            DbTask.title :request.title,
            DbTask.content : request.content,
            DbTask.status : request.status,
            DbTask.end : request.end,
            DbTask.creator_id : request.creator_id,
        }
    )
    db.commit()
    return "updated"