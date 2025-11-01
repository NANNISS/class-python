from flask import Flask
from cliente import cliente #importamos el blueprint desde el login.py


main = Flask(__name__)
main.register_blueprint(cliente) #registramos el blueprint

@main.route('/')
def home():
    return "Alanis Croce_2022200204 "
if __name__=='__main__':
    main.run(debug=True,port=5003,host='127.0.0.1')
    #comodin  app.run(debug=True,port=5000,host='0.0.0.0') para compartir 

from   flask import Blueprint, request, jsonify



    
