import uvicorn
from api.api import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.db.models import Base
from infrastructure.db.session import engine
from sqlalchemy_utils import create_database, database_exists

app = FastAPI(title="WriteForMe", openapi_url="/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)


def create_tables():
    print("create_tables")
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
