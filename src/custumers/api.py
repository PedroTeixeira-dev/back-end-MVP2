from flask_openapi3 import APIBlueprint, Tag

from src.custumers.models import Custumer
from src.custumers.schemas import CustumersPostSchema

custumers_api = APIBlueprint(
     "/custumers",
     __name__,
     url_prefix="/api",
     abp_tags=[Tag(name="Custumers", description="Random custumers")],
     doc_ui=True,
 )


@custumers_api.get("/custumers")
def get_custumers():
    return [{"id": custumer.id, "name": custumer.name} for custumer in Custumer.query.all()]


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
