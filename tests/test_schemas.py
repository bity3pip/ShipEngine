import pytest
from pydantic import ValidationError
from src.app.schemas.address import AddressCreate

def test_address_schema_valid():
    data = {
        "name": "John Doe",
        "address_line1": "123 Main St",
        "city_locality": "Austin",
        "state_province": "TX",
        "postal_code": "78701",
        "country_code": "US"
    }
    address = AddressCreate(**data)
    assert address.country_code == "US"

def test_address_schema_invalid_country():
    data = {
        "name": "John Doe",
        "address_line1": "123 Main St",
        "city_locality": "Austin",
        "state_province": "TX",
        "postal_code": "78701",
        "country_code": "USA"
    }
    with pytest.raises(ValidationError):
        AddressCreate(**data)