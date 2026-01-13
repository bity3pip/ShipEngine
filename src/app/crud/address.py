from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.app.models.address import Address
from src.app.schemas.address import AddressCreate

async def create_address(db: AsyncSession, address_in: AddressCreate):
    db_address = Address(**address_in.model_dump())
    db.add(db_address)
    await db.commit()
    await db.refresh(db_address)
    return db_address

async def get_address(db: AsyncSession, address_id: int):
    result = await db.execute(select(Address).where(Address.id == address_id))
    return result.scalar_one_or_none()

async def get_addresses(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Address).offset(skip).limit(limit))
    return result.scalars().all()