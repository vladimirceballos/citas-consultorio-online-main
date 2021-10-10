from app import db


class Profesional(db.Model):
    __tablename__='profesional'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    ocupacion = db.Column(db.String(120), unique=False, nullable=False)
