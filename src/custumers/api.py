from flask import request
from flask_openapi3 import APIBlueprint, Tag


from src.custumers.models import Custumer
from src.custumers.schemas import CustumerDeleteSchema, CustumersPostSchema, CustumersPutSchema

custumers_api = APIBlueprint(
     "/custumers",
     __name__,
     url_prefix="/api",
     abp_tags=[Tag(name="Custumers", description="Random custumers")],
     doc_ui=True,
 )


@custumers_api.get("/custumers")
def get_custumers():
    return [{"id": custumer.id, "name": custumer.name, "cep": custumer.cep, "email": custumer.email} for custumer in Custumer.query.all()]


@custumers_api.post("/custumers")
def create_custumer(body: CustumersPostSchema):
    print("#############", body)
    custumer = Custumer(
        name=body.name,
        email=body.email,
        cep=body.cep,
        uf=body.uf,
        city=body.city,
        street=body.street,
        number=body.number,
        complement=body.complement).save()
    return {"id": custumer.id, "name": custumer.name}


@custumers_api.delete("/custumers")
def delete_custumer(email: CustumerDeleteSchema):
    email = request.args.get('email')
    if not email:
        return {"error": "Email is required to delete a customer"}, 400

    custumer = Custumer.query.filter_by(email=email).first()
    if not custumer:
        return {"error": "Customer not found"}, 404

    custumer.delete()
    return {"message": "Customer deleted successfully"}


@custumers_api.put("/custumers")
def update_custumer(body: CustumersPutSchema):
    email = body.email
    custumer = Custumer.query.filter_by(email=email).first()
    if not custumer:
        return {"error": "Customer not found"}, 404

    custumer.name = body.name
    custumer.cep = body.cep
    custumer.uf = body.uf
    custumer.city = body.city
    custumer.street = body.street
    custumer.number = body.number
    custumer.complement = body.complement
    custumer.save()

    return {"id": custumer.id, "name": custumer.name}
