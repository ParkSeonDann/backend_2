from flask import Flask, send_from_directory

app = Flask(__name__)

# Configura la ruta de los archivos estáticos
app.config['STATIC_FOLDER'] = 'static'

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.config['STATIC_FOLDER'], path)

if __name__ == '__main__':
    app.run()