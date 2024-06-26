from flask_openapi3 import APIBlueprint, Tag


from src.custumers.models import Custumer
from src.custumers.schemas import CustumersPostSchema, CustumersResponseSchema, EmailPath

custumers_api = APIBlueprint(
     "/custumers",
     __name__,
     url_prefix="/api",
     abp_tags=[Tag(name="Custumers", description="Random custumers")],
     doc_ui=True,
 )


@custumers_api.get("/custumers")
def get_all_custumers():
    return [{"id": custumer.id, "name": custumer.name, "cep": custumer.cep, "email": custumer.email}
            for custumer in Custumer.query.all()]


@custumers_api.get("/custumers/<string:email>")
def get_custumer_by_email(path: EmailPath,
                          responses={200: CustumersResponseSchema}):
    custumer = Custumer.query.filter_by(email=path.email).first()
    if not custumer:
        return {"error": "Customer not found"}, 404

    return {
        "name": custumer.name,
        "cep": custumer.cep,
        "email": custumer.email,
        "uf": custumer.uf,
        "city": custumer.city,
        "street": custumer.street,
        "number": custumer.number,
        "complement": custumer.complement,
    }


@custumers_api.post("/custumers")
def create_custumer(body: CustumersPostSchema):
    custumer = Custumer(**body.dict()).save()
    return {"id": custumer.email, "name": custumer.name}


@custumers_api.delete("/custumers/<string:email>")
def delete_custumer(path: EmailPath):
    email = path.email
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
