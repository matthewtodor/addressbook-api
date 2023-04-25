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

@router.post('/', response_description = "Customer data added to the database")
async def add_customer(customer: CustomerSchema = Body(...)):
    customer = jsonable_encoder(customer)
    new_customer = await add_customer(customer)
    return ResponseModel(new_customer, "Customer added successfully")


router = APIRouter()