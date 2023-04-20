import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

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