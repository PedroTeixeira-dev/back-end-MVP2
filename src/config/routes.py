from flask import Blueprint, redirect

from src.custumers.api import custumers_api

root = Blueprint("root", __name__)


@root.route("/")
def index():
    return redirect("/docs")


apis = [custumers_api]
