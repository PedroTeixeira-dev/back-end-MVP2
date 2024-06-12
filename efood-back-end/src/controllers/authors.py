from flask_openapi3 import APIBlueprint, Tag

from src.models.authors import Author
from src.schemas.authors import AuthorPostSchema

author_api = APIBlueprint(
    "/authors",
    __name__,
    url_prefix="/api",
    abp_tags=[Tag(name="Authors", description="Random authors")],
    doc_ui=True,
)


@author_api.get("/authors")
def get_author():
    return [{"id": author.id, "name": author.name} for author in Author.query.all()]


@author_api.post("/authors")
def create_author(body: AuthorPostSchema):
    author = Author(name=body.name).save()
    return {"id": author.id, "name": author.name}
