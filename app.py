from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Esta función busca automáticamente en la carpeta 'templates'
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)