
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

from datetime import datetime
import socket
import sys

""" Decoradores:
Módulo que contiente los decoradores de la aplicación
"""
def decorador_registro(funcion):
    """ Decoradores
        Decorador de registro: se implementa al realizar una acción y
        toma los datos a fin de generar un registro de Log.

    Args:
        :funcion (function): "Función a decorar"

    Returns:
        function.
        Retorna una función denominada "Envoltura".
    """

    def envoltura(*args):
        """ Función de envoltura
        
        Args:
            :*args: Argumentos del método sobre el cual se aplica la función
             (list): Lista de argumentos
            
        Returns:
            :la devolución dependerá del método sobre el cual se aplica el decorador
        
        """

        fecha1 = datetime.now()
        fecha = fecha1.strftime("%d/%m/%Y %H:%M:%S")
        nombre_funcion = funcion.__name__
        texto = str(fecha) + ": Funcion utilizada: "+str(nombre_funcion)+", "
        
        if funcion.__name__ == "ingresar":
            data = []
            for i in range(1, len(args)-2):
                data.append(str(args[i].get()))
            texto = texto + "Datos ingresados: " + str(data)
            
        elif funcion.__name__ == "borrar":
            v = args[1].selection()
            i = args[1].item(v)
            data = i['values']
            texto = texto + "Datos eliminados: " + str(data)
            
        elif funcion.__name__ == "devolver":
            v = args[1].selection()
            i = args[1].item(v)
            data = i['values']
            texto = texto + "Datos devueltos: " + str(data)
        
        elif funcion.__name__ == "modificar":
            data = []
            for i in range(1, len(args)-1):
                data.append(str(args[i].get()))
            texto = texto + "Datos modificados: " + str(data)
    
        else:
            texto = texto + "Funcion Ejecutada"
    
        try:
            HOST, PORT = "localhost", 15200
            data = " ".join(sys.argv[1:])
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(texto.encode("UTF-8"), (HOST, PORT))
            recibido = sock.recvfrom(1024)
            print('Datos recibidos desde el Servidor', recibido)
               
        except:     
            print('Se ingresará a registro.txt: ',texto)      
            archivo = open("registro.txt", "a")
            archivo.write(texto + "\n")
            archivo.close()
        
        funcion(*args)
        
    return envoltura