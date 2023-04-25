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

@router.post("/", response_description="Customer data added to the database")
async def add_customer_data(customer: CustomerSchema = Body(...)):
    customer = jsonable_encoder(customer)
    new_customer = await add_customer(customer)
    return ResponseModel(new_customer, "Customer added successfully.")

@router.get("/", response_description="Customers received.")
async def get_customers():
    customers = await retrieve_customers()
    if customers:
        return ResponseModel(customers,"Customers data retrieved successfully")
    return ResponseModel(customers,"No Customer data found")

@router.get("/{id}" , response_description="Customer data successfully retrieved")
async def get_customer_data(id):
    customer = await retrieve_customer_by_id(id)
    if customer:
        return ResponseModel(customer, "Customer data retrieved successfully")
    return ResponseModel("Error:", 404, "Customer doesn't exist")


