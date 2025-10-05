from flask import Flask
from login import login #importamos el blueprint desde el login.py
from logout import logout

app = Flask(__name__)
app.register_blueprint(login) #registramos el blueprint
app.register_blueprint(logout)
@app.route('/')
def home():
    return "Hola, UNIDA experto en Python"
if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
    #comodin  app.run(debug=True,port=5000,host='0.0.0.0') para compartir 

