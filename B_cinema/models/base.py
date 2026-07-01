from . import db


class ModeloBase(db.Model):
    """Classe base abstrata: todo modelo ganha um id automático."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
