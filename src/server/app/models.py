from app import db

class UsuarioAdmin(db.Model):
    __tablename__ = 'usuariosadmin'
    curp = db.Column(db.String(18), primary_key=True)
    nombre = db.Column(db.String(50))
    apellido_paterno = db.Column(db.String(50))
    apellido_materno = db.Column(db.String(50))
    numero_telefono = db.Column(db.String(15))
    correo = db.Column(db.String(100))
    direccion = db.Column(db.String(255))
    colonia = db.Column(db.String(100))
    municipio = db.Column(db.String(100))
    codigo_postal = db.Column(db.String(5))
    contraseña = db.Column(db.String(255))

    def to_dict(self):
        return {
            'curp': self.curp,
            'nombre': self.nombre,
            'apellido_paterno': self.apellido_paterno,
            'apellido_materno': self.apellido_materno,
            'numero_telefono': self.numero_telefono,
            'correo': self.correo,
            'direccion': self.direccion,
            'colonia': self.colonia,
            'municipio': self.municipio,
            'codigo_postal': self.codigo_postal
        }
