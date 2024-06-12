from src.config.database import db
from src.core.models import BaseModel


class Author(BaseModel):
    __tablename__ = "authors"

    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<id {self.id}>"
