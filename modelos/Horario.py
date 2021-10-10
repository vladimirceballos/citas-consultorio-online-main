from app import db


class Horario (db.Model):
    __tablename__='horarios'
    id = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.String(120), unique=False, nullable=False)

def crear_horario(horario):
    hora = horario['hora']
    

    hora = hora (hora=hora) 
    db.session.add(cita)
    db.session.commit()
    return False