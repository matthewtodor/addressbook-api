from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from app.server.database import (
    add_customer,
    delete_customer,
    retrieve_customers,
    retrieve_customer_by_id,
    update_customer,
)
from app.server.models.customer import (
    ErrorResponseModel,
    ResponseModel,
    CustomerSchema,
    UpdateCustomerModel
)

router = APIRouter()