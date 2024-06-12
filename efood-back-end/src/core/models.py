from datetime import datetime

from src.config.database import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    updated_at = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)

    def save(self, **kwargs):
        model = self.__class__(name=self.name)
        db.session.add(model)
        db.session.commit()
        return model
