from fastapi import FastAPI
from horras_backend.api.v1 import router as api_router
from horras_backend.database import prisma

app = FastAPI(
    title="Horras Backend",
    description="Backend for Horras",
    version='0.1.0', 
)

app.include_router(api_router, prefix="/api/v1", tags=["api"])

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}