# from flask_openapi3 import APIBlueprint, Tag

# from src.books.models import Book
# from src.books.schemas import BookPostSchema

# book_api = APIBlueprint(
#     "/books",
#     __name__,
#     url_prefix="/api",
#     abp_tags=[Tag(name="Book", description="Some Book")],
#     doc_ui=True,
# )


# @book_api.get("/books")
# def get_book():
#     return [{"id": book.id, "name": book.name} for book in Book.query.all()]


# @book_api.post("/books")
# def create_book(body: BookPostSchema):
#     book = Book(name=body.name).save()
#     return {"id": book.id, "name": book.name}
