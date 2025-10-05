from   flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)
@login.route('/login', methods=['POST'])
def login_user(): #función
    #print("Headers:", request.headers)
    #print("Body:", request.json)
    user = request.json.get('user')
    password = request.json.get('password')
    matricula = request.json.get('matricula')
    print("Headers:", request.headers)
    print(f"Usuario: {user}, passwor: {password}, Matricula: {matricula}")

    codRes,menRes,accion=inicializarVariables(user, password) #llama a la función
    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "user": user,
        "accion": accion
    }
    return jsonify(salida)
def inicializarVariables(user, password):
    userLocal = "alanisc"
    passLocal = "unida123"
    codeRes= "sin error"
    menRes= "ok"
    
    try:
        print("verificar login")
        if user == userLocal and password == passLocal:
            print("Login exitoso")
            accion="Succes"
        else:
            print("usuario o password incorrecto")
            codRes="ERROR"
            menRes= "usuario o password incorrecto"
            print("login fallido")
            accion="Not Succes"
    except Exception as e: #todo se guarda en e
        print("ERROR",str(e))
        codRes="ERROR"
        menRes= 'Msg:' +str(e)
        accion= "Error interno"

    return codeRes, menRes, accion

