from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    datos={'Usuarios':120, 'Ventas':4720,'Visitas':3080}
    return render_template('home.html', datos=datos)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
else:
    print("El Servidor Está Corriendo...")