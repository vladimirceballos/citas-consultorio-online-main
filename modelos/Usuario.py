from app import db 


class Usuario (db.Model):
    
    __tablename__='usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(255), unique=False, nullable=False)
    documento = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    genero = db.Column(db.String(120), unique=False, nullable=False)
    edad = db.Column(db.Integer, unique=False, nullable=False)
    contrasena = db.Column(db.String(120), unique=False, nullable=False)
    perfil = db.Column(db.Integer, db.ForeignKey(
        'perfil.id'), nullable=False)
    correo = db.Column(db.String(120), unique=False, nullable=False)
    telefono = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "<Usuario: {}, {}>".format(self.id, self.nombre)


def crear_usuario(usuario):
    tipo_documento = usuario['tipo_documento']
    documento = int(usuario['documento'])
    nombre = usuario['nombre']
    genero = usuario['genero']
    edad = int(usuario['edad'])
    telefono = int(usuario['telefono'])
    correo = usuario['correo']
    contrasena = usuario['contrasena']

    usuario = Usuario(tipo_documento=tipo_documento,
                    documento=documento,
                    nombre=nombre,
                    genero=genero,
                    edad=edad,
                    contrasena=contrasena,
                    perfil=3,
                    correo=correo,
                    telefono=telefono)
    db.session.add(usuario)
    db.session.commit()
    return False
