from flask import Flask, render_template

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal (el "muro" de Cuaji-Posts)
@app.route('/')
def home():
    # Por ahora, solo mostraremos un mensaje de bienvenida
    return """
    <h1>¡Bienvenido a Cuaji-Posts!</h1>
    <p>Proyecto de Ingeniería de Software II - UAM Cuajimalpa</p>
    <ul>
        <li>Estado del servidor: <b>Activo</b></li>
        <li>Próximo paso: Configurar el Módulo de Registro</li>
    </ul>
    """

# Arrancamos el servidor en modo de prueba (debug)
if __name__ == '__main__':
    app.run(debug=True)