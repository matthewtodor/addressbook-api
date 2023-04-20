from typing import Optional

from pydantic import BaseModel, Field



class CustomerSchema(BaseModel):
    firstName: str = Field(...)
    lastName: str = Field(...)
    streetAddress: str = Field(...)
    streetAddress2: str = Field(...) | None
    city: str = Field(...)
    # if country code is not USA, state and zipcode can be used for country-specific values that are equivalents
    state: str = Field(...) | None
    zipcode: int = Field(...) | None
    # If not provided, country code defaults to USA country code (ISO 3166 standard) (USA: US)
    country: str = Field(...) | None

    
    class Config: 
        schema_extra = {
            "example": {
            "firstName" : "Mary",
            "lastName" : "Douglass",
            "streetAddress": "15566 Michigan Ave",
            "streetAddress2": "Unit C",
            "city": "Columbus",
            "state": "Ohio",
            "zipcode": 43004,
            "country": "US"
            }
        }
