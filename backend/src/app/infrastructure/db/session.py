from typing import Generator

from infrastructure.config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = config.DB_SETTINGS.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = session()
        yield db
    finally:
        db.close()
