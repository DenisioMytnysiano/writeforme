import uvicorn
from api.api import api_router
from fastapi import FastAPI
from infrastructure.db.models import Base
from infrastructure.db.session import engine
from sqlalchemy_utils import database_exists, create_database

app = FastAPI(title="WriteForMe", openapi_url=f"/openapi.json")

app.include_router(api_router)

def create_tables():
  print("create_tables")
  if not database_exists(engine.url):
    create_database(engine.url)
  Base.metadata.create_all(bind=engine)
        
if __name__ == "__main__":
    create_tables()
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)