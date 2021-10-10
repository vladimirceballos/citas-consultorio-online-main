from app import db
from modelos.Usuario import Usuario
from flask import request


class Cita(db.Model):
    
    __tablename__='cita'
    
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.String(120), unique=False, nullable=False)
    sede = db.Column(db.String(120), unique=False, nullable=False)
    profesional = db.Column(db.String(120), unique=False, nullable=False)
    id_horario = db.Column(db.Integer, db.ForeignKey(
        'horario.id'), nullable=False)
    id_sede = db.Column(db.Integer, db.ForeignKey(
        'sede.id'), nullable=False)
    id_profesional = db.Column(db.Integer, db.ForeignKey(
        'profesional.id'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey(
        'usuario.id'), nullable=True)
    asignada = db.Column(db.Boolean, unique=False, nullable=True)
    diagnostico = db.Column(db.String(120), unique=False, nullable=True)
    medicamentos = db.Column(db.String(120), unique=False, nullable=True)

def crear_cita(cita):
    horario = cita['horario']
    sede = cita['sede']
    profesional = cita['profesional']

    cita = Cita(horario=horario,
                    sede=sede,
                    profesional=profesional,)
    db.session.add(cita)
    db.session.commit()
    return False
    
@staticmethod   
def agendar_cita(cita):
    cita_seleccionada= Cita.query.filter_by(id=id_cita)
    cita_seleccionada.id_usuario= ['id_usuario']
    db.session.commit()
    
    
@staticmethod   
def list_historial(cita):
    historial=[]
    historial=Cita.query.with_entities(Cita.id, Cita.horario, Cita.sede, Cita.profesional, Cita.medicamentos,Cita.diagnostico).filter_by(Cita.id_usuario)
    return(historial)
    
    
@staticmethod
def add_historial(cita):
    cita=Cita.query.get.filter_by(id=id_cita)
    print(cita)
    cita.medicamentos= request.form['medicamentos']
    cita.diagnostico= request.form['diagnostico']
    db.session.commit()
    
    