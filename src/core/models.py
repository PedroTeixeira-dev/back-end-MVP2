import uuid

from datetime import datetime

from src.config.database import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.UUID(), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    updated_at = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)

    def save(self, **kwargs):
        db.session.add(self)
        db.session.commit()
        return self
