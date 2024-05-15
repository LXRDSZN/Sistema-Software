from flask import jsonify, request, abort, current_app as app
from app import db
from app.models import UsuarioAdmin

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    app.logger.debug(f'Received data: {data}')
    curp = data.get('curp')
    contraseña = data.get('contraseña')
    
    user = UsuarioAdmin.query.filter_by(curp=curp).first()
    app.logger.debug(f'User found: {user}')
    
    if user and user.contraseña == contraseña:
        app.logger.debug('Login successful')
        return jsonify({'message': 'Login exitoso', 'user': user.to_dict()})
    else:
        app.logger.debug('Invalid credentials')
        return abort(401, description='Credenciales inválidas')
