from src.app.crud import address as crud_address
from src.app.schemas.address import AddressCreate


async def test_create_address_crud(db_session):
    address_in = AddressCreate(
        name="Test User",
        address_line1="123 Street",
        city_locality="London",
        state_province="Greater London",
        postal_code="SW1A 1AA",
        country_code="GB"
    )

    db_address = await crud_address.create_address(db_session, address_in)
    assert db_address.id is not None
    assert db_address.country_code == "GB"