from flask import Flask, jsonify, request
from distutils.log import debug
from config import config
from flask_mysqldb import MySQL
import json
import os

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/access/login', methods = ['GET'])
def login():
    correo = {"correo": request.json['nombre']}
    contraseña = {"contraseña": request.json['contraseña']}
    cursor = conexion.connection.cursor()
    sql = 'IF EXISTS (SELECT correo, contraseña FROM usuario WHERE correo = %s AND contraseña = %s)'(correo, contraseña)
    cursor.execute(sql)
    respuesta = bool(cursor.fetchall())
    conexion.connection.commit()
    if respuesta == True:
        cursor = conexion.connection.cursor()
        sql = 'SELECT nombre FROM usuario WHERE correo = %s )'(correo)
        cursor.execute(sql)
        nombre = cursor.fetchall()
        return jsonify({"nombre": nombre})
    else: 
        return jsonify({"message": "No esta registrado"})

@app.route('/access/registro', methods = ['POST'])
def registrar():
    nombre = {"nombre": request.json['nombre']}
    correo = {"correo": request.json['correo']}
    contraseña = {"contraseña": request.json['contraseña']}
    cursor = conexion.connection.cursor()
    query = 'INSERT INTO usuario VALUES (%s, %s, %s)',(nombre, correo, contraseña)
    cursor.execute(query)
    respuesta = bool(cursor.fetchall())
    conexion.connection.commit()
    if respuesta == True:
        cursor = conexion.connection.cursor()
        sql = 'SELECT nombre FROM usuario WHERE correo = %s )'(correo)
        cursor.execute(sql)
        nombre = cursor.fetchall()
        return jsonify({"message": "Registrado con exito"})
    else: 
        return jsonify({"message": "Error al registrar"})

@app.route('/access/cargar-archivo/', methods = ['GET'])
def recibir_archivo():
    archivo = request.files['files']
    nombre_archivo = os.path.basename(archivo)
    archivo.save(os.path.join(app.config.from_object(config['desarrollo']), nombre_archivo))
    pass


if __name__ == '__main__':
    app.config.from_object(config['desarrollo'])
    app.run()

