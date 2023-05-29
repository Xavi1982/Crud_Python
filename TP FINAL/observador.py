# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

from tkinter import messagebox


class Subject:
    """Clase Subjet
    
    Definimos los métodos de los observadores.

    1- Método agregar \
    2- Método quitar \
    3- Método notificar \
    
    """

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        self.observadores.remove(obj)

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class Observador:
    def update(
        self,
    ):
        raise NotImplementedError("Delegacion de actualización")


class ConcreteObserver_A(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("Actualizacion dentro de Observador Concreto A")
        print("Aqui estan los parametros: ", args)
        x = args[0][0]
        if int(x) % 20 == 0:
            messagebox.showinfo(
                "AVISO",
                "Es posible que sus estadísticas hayan cambiado, revise el menú",
            )
        else:
            print("Observador Ejecutado")

    def contador(
        self,
    ):
        pass
