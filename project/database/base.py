import os

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from project.config import settings

# Генерація шляху до цієї папки
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
# Створення шляху до папки,у якій буде міститись база даних проекту
db_path = os.path.join(BASE_DIR, 'project', 'database', 'DB')
# Якщо такої немає, то створити
if not os.path.exists(db_path):
    os.makedirs(db_path)

# Базові налашутвання і дані, необхідні для роботи бази даних
Base = declarative_base()

# Створення двигуна бази даних
engine = create_engine(settings.db_url, connect_args={"check_same_thread": False}, echo=True)


def get_db():
    """
    Функція,яка створює екземпляри сесії для кожного підключення до БД
    """
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()


# Створення сесії БД
SessionLocal = sessionmaker(autoflush=False, bind=engine)
