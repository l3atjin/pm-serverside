from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Project(Base):
  __tablename__ = "projects"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(50), unique=True, index=True)