from fastapi import FastAPI
from src.app.api.v1 import addresses
from src.app.core.db.database import engine, Base
app = FastAPI(title="ShipEngine CRUD API")
app.include_router(addresses.router, prefix="/api/v1")


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
