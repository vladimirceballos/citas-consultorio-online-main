from app import db


class Sede(db.Model):
    __tablename__='sede'
    
    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(120), unique=False, nullable=False)
    ciudad = db.Column(db.String(120), unique=False, nullable=False)
    departamento = db.Column(db.String(120), unique=False, nullable=False)
    comuna = db.Column(db.String(120), unique=False, nullable=True)
    direccion = db.Column(db.String(120), unique=False, nullable=False)
