from fastapi import FastAPI, Request
from db import models
from db.database import engine
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication
from routers import user

app = FastAPI()
app.include_router(user.router)
app.include_router(authentication.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}


models.Base.metadata.create_all(engine)

