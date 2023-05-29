
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

from peewee import *

# CREACION CLASE DE BASE DATOS (TIPO DE BASE)
""" Creación de la base de datos.

Nuestra base de datos es del tipo SQLite3.
El archivo que corresponderá a la base se llamará: *database.db*.
Nos permite manejar a traves del ORM la conexión con la base de datos.

"""
db = SqliteDatabase('database.db')
class BasePeewee(Model):
    """Clase BasePeewee.
    Hereda de Modelo.

    """
    class Meta:
        database=db
        
# CREACION CLASE DE TABLA       
class Registro(BasePeewee):
    """Clase Registro.
    Hereda de la Clase *BasePeewee*.
    
    :prod=CharField()
    :cant=DoubleField()
    :prec=DoubleField()
    
    """
    prod=CharField()
    cant=DoubleField()
    prec=DoubleField()
  
db.connect()
db.create_tables([Registro])