from typing import Annotated
from fastapi import FastAPI, Depends
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ProjectBase(BaseModel):
  name: str


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/projects/")
async def create_project(project: ProjectBase, db: db_dependency):
  db_project = models.Project(name=project.name)
  db.add(db_project)
  db.commit()
  db.refresh(db_project)
  return db_project


@app.get("/projects/")
async def read_projects(db: db_dependency):
  projects = db.query(models.Project).all()
  return projects

@app.get("/projects/{project_id}")
async def read_project(project_id: int, db: db_dependency):
  project = db.query(models.Project).filter(models.Project.id == project_id).first()
  return project

@app.get("/")
async def root():
  return {"message": "Hello World"}



@app.get("/hello/{name}")
async def say_hello(name: str):
  return {"message": f"Hello {name}"}