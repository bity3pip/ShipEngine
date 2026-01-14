from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from src.app.core.db.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[Optional[str]]
    company_name: Mapped[Optional[str]]
    address_line1: Mapped[str] = mapped_column(nullable=False)
    address_line2: Mapped[Optional[str]]
    city_locality: Mapped[str] = mapped_column(nullable=False)
    state_province: Mapped[str] = mapped_column(nullable=False)
    postal_code: Mapped[str] = mapped_column(nullable=False)
    country_code: Mapped[str] = mapped_column(nullable=False)
    is_residential: Mapped[Optional[bool]] = mapped_column(default=False)
