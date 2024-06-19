from src.config.database import db
from src.core.models import BaseModel


class Custumer(BaseModel):
    __tablename__ = "custumers"

    email = db.Column(db.String(30))
    name = db.Column(db.String(50))
    cep = db.Column(db.String(8))
    uf = db.Column(db.String(10))
    city = db.Column(db.String(30))
    street = db.Column(db.String(40))
    number = db.Column(db.Integer())
    complement = db.Column(db.String(100), nullable=True)

    def __init__(self, email, name, cep, uf, city, street, number, complement):
        self.email = email
        self.name = name
        self.cep = cep
        self.uf = uf
        self.city = city
        self.street = street
        self.number = number
        self.complement = complement

    def __repr__(self):
        return f"<id {self.id}>"

    def save(self, **kwargs):
        model = self.__class__(
            name=self.name,
            email=self.email,
            cep=self.cep,
            uf=self.uf,
            city=self.city,
            street=self.street,
            number=self.number,
            complement=self.complement)
        db.session.add(model)
        db.session.commit()
        return model
