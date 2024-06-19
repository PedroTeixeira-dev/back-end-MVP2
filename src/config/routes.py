from flask import Blueprint, redirect

# from src.authors.api import author_api
# from src.books.api import book_api

from src.custumers.api import custumers_api

root = Blueprint("root", __name__)


@root.route("/")
def index():
    return redirect("/docs")


apis = [custumers_api]
