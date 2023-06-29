import pymysql

class Configuraciones():
    DEBUG = True
    MYSQL_HOST='localhost',
    MYSQL_USER='root',
    MYSQL_PASSWORD='1234',
    MYSQL_DB='usuarios'

config = {
    'desarrollo': Configuraciones
}