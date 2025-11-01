from flask import blueprints, request, jsonify
cliente = blueprints.Blueprint('cliente', __name__)

cliente_db = {
   "5305710" : { 
        "nombre": "Alanis",
        "apellido": "Croce",
        "celular": "0982525252",
        "direccion": "Av. Siempre Viva 742"
    }
}

@cliente.route('/cliente', methods=['POST'])
def buscar_cliente():
    try:
        datos = request.json
        ci = datos.get('ci')
        if not ci:
            return jsonify({
                "accion": "cliente no esta en el sistema",
                "codRes": "ERROR",
                "menRes": "error cliente",
                "ci": ""
            }), 400
        
        if ci in cliente_db:
            cliente_info = cliente_db[ci]
            return jsonify({
                "accion": "Succes",
                "codRes": "sin error",
                "menRes": "ok",
                "ci": ci,
                "nombre": cliente_info["nombre"],
                "apellido": cliente_info["apellido"],
                "celular": cliente_info["celular"],
                "direccion": cliente_info["direccion"]
            }), 200
        else:
            return jsonify({
                "accion": "cliente no esta en el sistema",
                "codRes": "ERROR",
                "menRes": "error cliente",
                "ci": ci
            }), 404
    except Exception as e:
        return jsonify({
            "accion": "error",
            "codRes": "ERROR",
            "menRes": f"Msg: {str(e)}",
            "ci": ""
        }), 500
        