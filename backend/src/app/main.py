import uvicorn
from api.api import api_router
from fastapi import FastAPI

app = FastAPI(title="WriteForMe", openapi_url=f"/openapi.json")

app.include_router(api_router)

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
