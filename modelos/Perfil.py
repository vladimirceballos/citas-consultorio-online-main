from app import db


class Perfil (db.Model):
    __tablename__='perfil'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    descripcion = db.Column(db.String(120), unique=False, nullable=False)
