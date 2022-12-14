from sqlalchemy import Column, Integer, String, Boolean

from project.database.base import Base, engine


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
