from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import re


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

regex = "^[0-9a-f]{24}+$"
id_reg = re.compile(regex)

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
async def get_customer_data(id:str):
    if re.match(id_reg, id):
        customer = await retrieve_customer_by_id(id)
        if customer:
            return ResponseModel(customer, "Customer data retrieved successfully")
        return ErrorResponseModel("Error:", 404, "Customer doesn't exist")
    
    return ErrorResponseModel("Error:", 503, "The provided id ({}) is not valid".format(id))

@router.put("/{id}")
async def update_customer_data(id:str, req:UpdateCustomerModel=Body(...)):
    if re.match(id_reg, id):
        req = {k:v for k, v in req.dict().items() if v is not None}
        updated_customer = await update_customer(id, req)
        if updated_customer:
            return ResponseModel(
                "Customer with id: {} update is successful".format(id),
                "Customer updated successfully",
            )
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error updating the customer data. Please check the information and try again. If this continues, please contact the administrator."
        )
    return ErrorResponseModel("Error:", 503, "The provided id ({}) is not valid".format(id))

@router.delete("/{id}", response_description="Customer data deleted from the database")
async def delete_customer_data(id:str):
    if re.match(id_reg, id):
        deleted_customer = await delete_customer(id)
        if deleted_customer:
            return ResponseModel(
                "Customer was successfully deleted!",
                "Customer deletion successful"
            )
        return ErrorResponseModel("An error occurred", 404, "There was an error deleting the customer data. Please check the information and try again. If this continues, please contact the administrator.")
    return ErrorResponseModel("Error:", 503, "The provided id ({}) is not valid".format(id))
