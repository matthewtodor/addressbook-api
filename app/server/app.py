from fastapi import FastAPI

from app.server.routes.customer import router as CustomerRouter

app = FastAPI()

app.include_router(CustomerRouter, tags=["Customer"], prefix="/customer")



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hi Jesse"}