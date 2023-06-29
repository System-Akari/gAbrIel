from flask import Flask, jsonify, request
from distutils.log import debug
from config import config


app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/cargar-archivo/<archivo>', methods = ['GET'])
def recibir_archivo(archivo):
    return 


if __name__ == '__main__':
    app.config.from_object(config['desarrollo'])
    app.run()

