from flask import Flask
app= Flask(__name__)

@app.route('/')
def home():
    return "Hola, UNIDA experto en Python"
if __name__=="__main__":
    app.run(debug=True,port=5000,host='127.0.0.1')
    #comodin  app.run(debug=True,port=5000,host='0.0.0.0') para compartir 

