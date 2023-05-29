
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

from pathlib import Path
import os
import sys
import subprocess
import threading

proceso = ""

class Server:
    """ Clase Server:

    Permite la conexión y desconexión con el servidor.

    """
    def __init__(self, ):
        """Constructor de la Clase Server.

        Se establece en él la ruta al archivo donde se ubica el servidor.

        """
        self.root = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.root,'servidor','upd_servidor.py')
        
    def prender(self, ):
        print('Iniciando Servidor...')
        
    def try_connection(self, ):
        """Método que permite establecer la conexión con el servidor.

        """
        self.prender()
        if proceso != "":
            proceso.kill()
            threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
        
        else:
            threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
 

            
    def lanzar_servidor(self, var):
        """Método que permite el lanzamiento del servidor.
        
        Args:
            :*var: variable, True or False.
                  Por defecto se establece el valor en "True".
            :type: Boolean

        Returns: Establece la conexión con el servidor.

        """
        el_path = self.ruta_server
        if var == True:
            global proceso
            proceso = subprocess.Popen([sys.executable, el_path])
            proceso.communicate()
        else:
            print("No se pudo comunicar con el servidor")
            
    def stop_server(self, ):
        """Método que permite la desconexión del servidor.
        
        """
        if proceso != "":
            proceso.kill()
            print("Se apagó el servidor")