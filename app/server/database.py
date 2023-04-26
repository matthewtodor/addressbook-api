import motor.motor_asyncio

from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.customers

customer_collection = database.get_collection("customers_collection")




#helpers

def customer_helper(customer) -> dict:
    return {
        "id": str(customer["_id"]),
        "firstName": customer["firstName"],
        "lastName": customer["lastName"],
        "streetAddress": customer["streetAddress"],
        "streetAddress2": customer["streetAddress2"],
        "city": customer["city"],
        "state": customer["state"],
        "zipcode": customer["zipcode"],
        "country": customer["country"]
    }

# get all customers
async def retrieve_customers():
    customers = []
    async for customer in customer_collection.find():
        customers.append(customer_helper(customer))
    return customers

# get customer by ID
async def retrieve_customer_by_id(id:str) -> dict:
    customer = await customer_collection.find_one({"_id" : ObjectId(id)})
    if customer:
        return customer_helper(customer)
    
# Add new customer
async def add_customer(customer_data:dict) -> dict:
    customer = await customer_collection.insert_one(customer_data)
    new_customer = await customer_collection.find_one({"_id" : customer.inserted_id})
    return customer_helper(new_customer)


# Update customer
async def update_customer(id:str, data:dict):
    if len(data) < 1:
        return False
    customer = await customer_collection.find_one({"_id" : ObjectId(id)})
    if customer:
        updated_customer = await customer_collection.update_one(
            {"_id" : ObjectId(id)}, {"$set" : data}
        )
        if updated_customer:
            return True
        return False
    
# Delete customer
async def delete_customer(id:str):
    customer = await customer_collection.find_one({"_id" : ObjectId(id)})
    if customer:
        await customer_collection.delete_one({"_id" : ObjectId(id)})
        return True
