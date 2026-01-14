from typing import List

from arq.connections import ArqRedis
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core.db.database import get_db, get_arq_pool
from src.app.crud import address as crud_address
from src.app.schemas.address import AddressCreate, AddressRead

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.post("/", response_model=AddressRead)
async def create_new_address(
        address_in: AddressCreate,
        db: AsyncSession = Depends(get_db),
        arq_pool: ArqRedis = Depends(get_arq_pool)):

    new_address = await crud_address.create_address(db, address_in)

    await arq_pool.enqueue_job("validate_address_task", new_address.id)

    return new_address

@router.get("/{address_id}", response_model=AddressRead)
async def read_address(address_id: int, db: AsyncSession = Depends(get_db)):
    db_address = await crud_address.get_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.get("/", response_model=List[AddressRead])
async def read_addresses(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud_address.get_addresses(db, skip, limit)