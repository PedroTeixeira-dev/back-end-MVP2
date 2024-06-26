from src.config.database import db
from src.core.models import BaseModel


class Custumer(BaseModel):
    __tablename__ = "custumers"

    email = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(50))
    cep = db.Column(db.String(8))
    uf = db.Column(db.String(10))
    city = db.Column(db.String(30))
    street = db.Column(db.String(40))
    number = db.Column(db.Integer())
    complement = db.Column(db.String(100), nullable=True)

    def update(self, **kwargs):
        model = self.__class__(
            name=self.name,
            email=self.email,
            cep=self.cep,
            uf=self.uf,
            city=self.city,
            street=self.street,
            number=self.number,
            complement=self.complement
            )
        db.session.commit()
        return model

    def delete(self):
        db.session.delete(self)
        db.session.commit()
