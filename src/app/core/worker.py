import asyncio
import logging
import os

from arq.connections import RedisSettings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def validate_address_task(ctx, address_id: int):
    logger.info(f"Start address validation with ID: {address_id}")

    # Simulate validation

    await asyncio.sleep(5)

    logger.info(f"Address {address_id} successfully validated!")
    return True


class WorkerSettings:
    functions = [validate_address_task]
    redis_settings = RedisSettings(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=os.getenv("REDIS_PORT", 6379),)