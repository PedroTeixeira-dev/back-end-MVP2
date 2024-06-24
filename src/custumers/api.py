from flask_openapi3 import APIBlueprint, Tag
from flask_cors import CORS


from src.custumers.models import Custumer
from src.custumers.schemas import CustumerDeleteSchema, CustumersPostSchema

custumers_api = APIBlueprint(
     "/custumers",
     __name__,
     url_prefix="/api",
     abp_tags=[Tag(name="Custumers", description="Random custumers")],
     doc_ui=True,
 )
CORS(custumers_api, origins="http://localhost:3000")


@custumers_api.get("/custumers")
def get_custumers():
    return [{"id": custumer.id, "name": custumer.name, "cep": custumer.cep, "email": custumer.email} for custumer in Custumer.query.all()]


@custumers_api.post("/custumers")
def create_custumer(body: CustumersPostSchema):
    custumer = Custumer(**body.dict()).save()
    return {"id": custumer.id, "name": custumer.name}


@custumers_api.delete("/custumers/")
def delete_custumer(body: CustumerDeleteSchema):
    email = body.email
    if not email:
        return {"error": "Email is required to delete a customer"}, 400

    custumer = Custumer.query.filter_by(email=email).first()
    if not custumer:
        return {"error": "Customer not found"}, 404

    custumer.delete()
    return {"message": "Customer deleted successfully"}


@custumers_api.put("/custumers")
def update_custumer(body: CustumersPostSchema):
    email = body.email
    print(f"Received request to update customer with email: {email}")

    custumer = Custumer.query.filter_by(email=email).first()
    if not custumer:
        print("Customer not found")
        return {"error": "Customer not found"}, 404

    print(f"Updating customer: {custumer}")

    try:
        # Print the received body to debug
        print("Received body:", body)

        custumer.name = body.name
        custumer.cep = body.cep
        custumer.uf = body.uf
        custumer.city = body.city
        custumer.street = body.street
        custumer.number = body.number
        custumer.complement = body.complement

        custumer.update()
        print(f"Customer updated successfully: {custumer}")
    except Exception as e:
        print(f"An error occurred while updating the customer: {str(e)}")
        return {"error": f"An error occurred while updating the customer: {str(e)}"}, 500

    return {"id": custumer.id, "name": custumer.name}
