class Configuraciones():
    DEBUG = True
    PORT = 5000
    MYSQL_HOST = 'localhost',
    MYSQL_USER = 'root',
    MYSQL_PASSWORD = 'admin1234',
    MYSQL_DB = 'usuarios'
    UPLOAD_FOLDER = './archivos/original'

config = {
    'desarrollo': Configuraciones
}