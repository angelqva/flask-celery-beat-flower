from settings import constants
from sqlalchemy import inspect

db = constants.db


class Beer(db.Model):
    id = db.Column(db.String(50), primary_key=True,
                   nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    style = db.Column(db.String(50))

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.email

    __table_args__ = (db.UniqueConstraint(
        'name', 'style', name='_name_style_uc'),)
