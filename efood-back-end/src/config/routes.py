from flask import Blueprint, redirect

# from src.authors.api import author_api
# from src.books.api import book_api

from src.controllers.authors import author_api
from src.controllers.books import book_api

root = Blueprint("root", __name__)


@root.route("/")
def index():
    return redirect("/docs")


apis = [author_api, book_api]
