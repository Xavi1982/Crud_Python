
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

from tkinter import Tk
from vista import VistaVentana
import observador


class Controlador:
    """ Controlador

    Módulo que permite lanzar la aplicación

    """

    def __init__(self, raiz):
        """ Constructor de la clase

        Args:
            :controlador: Ventana raíz de la aplicación
                        (Interfaz gráfica del usuario)
            :observadora: Observador A

        """

        self.raiz = raiz
        self.obj_vista = VistaVentana(self.raiz)
        self.el_observadora = observador.ConcreteObserver_A(self.obj_vista.obj)


if __name__ == "__main__":
    root = Tk()
    Controlador(root)
    root.mainloop()
