
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

from tkinter import StringVar
from modelo import Modelo
from cls.vista_app import VistaApp
from cls.estilos.estilo import estilos

# CLASE VISTAVENTANA CREA LA VENTANA DE TKINTER,
# USANDO LOS OBJETOS DE LA CLASE VISTAAPP PARA LOS WIDGETS Y
# LOS OBJETOS DE MODELO PARA LA FUNCIONALIDAD

class VistaVentana():
    # CONSTRUCTOR DE LA CLASE
    """Clase VistaVentana.
    """
    def __init__(self, raiz, ):
        """Método constructor de la Clase VistaVentana.
        
        Args:
            :raiz: Ventana raíz de la aplicación
                    (Interfaz gráfica del usuario).
            
        Returns:
            :Nos retorna la interfáz gráfica del usuario.
            
            """
        self.raiz=raiz
        
        # VARIABLES DE TKINTER
        self.prod = StringVar()
        self.cant = StringVar()
        self.prec = StringVar()
        
        # LISTA CREADA PARA PODER SETEAR LOS ENTRIES EN UN STRING VACíO ("")
        self.campos = [self.prod,
                       self.cant,
                       self.prec]
        
        # VARIABLE DE TKINTER PARA FUNCIONALIDAD DE RADIOBUTTON
        self.opcion = StringVar()
        
        # OBJETO DE CLASE MODELO EJECUTA LAS FUNCIONES DECLARADAS EN MODELO
        self.obj = Modelo()
        
        # OBJETOS DE CLASE VISTAAPP CREAN LOS WIDGETS PARA LA VENTANA
        self.obj2= VistaApp(self.raiz)
        self.obj3=VistaApp(self.raiz)
        self.obj4=VistaApp(self.raiz)
        self.obj5=VistaApp(self.raiz)
        self.obj6=VistaApp(self.raiz)
        self.obj7=VistaApp(self.raiz)
        self.obj8=VistaApp(self.raiz)
        self.obj9=VistaApp(self.raiz)
        self.obj10=VistaApp(self.raiz)
        
        # LISTA CREADA PARA DEVOLVER LOS VALORES CON LA FUNCIóN SELECCION A LOS ENTRIES
        self.lista = [self.obj5,
                      self.obj6,
                      self.obj7]
        
        # OBJETO CORRESPONDIENTE AL LISTBOX
        self.obj2.lista()
        
        # OBJETO CORRESPONDIENTE AL TREEVIEW
        self.obj3.tablap()
        
        # OBJETOS CORRESPONDIENTES A LOS LABELS
        self.obj8.etiqueta('Producto', 1, 16, 's')
        self.obj9.etiqueta('Cantidad', 3, 16, 's')
        self.obj10.etiqueta('Precio', 5, 16, 's') 
        
        # OBJETOS CORRESPONDIENTES A LOS ENTRIES
        self.obj5.caja(35, self.prod, 2, 16, 3, 's', 5)
        self.obj6.caja(35, self.cant, 4, 16, 3, 's', 5)
        self.obj7.caja(35, self.prec, 6, 16, 3, 's', 5)
        
        # OBJETO CORRESPONDIENTE AL MENú
        self.obj4.menu()
        
        # OBJETOS CORRESPONDIENTES A LOS BOTONES
        self.obj2.boton('Ingreso', 18, 16, 'nsew', lambda:self.obj.ingresar(self.prod,
                                                                            self.cant,
                                                                            self.prec,
                                                                            self.obj3.tabla,
                                                                            self.campos))
        
        self.obj2.boton('Consulta', 18, 17, 'nsew', lambda:self.obj.consultar(self.obj3.tabla))
        
        self.obj2.boton('Eliminar', 18, 18, 'nsew', lambda:self.obj.borrar(self.obj3.tabla))
        
        self.obj2.boton('Modificar', 20, 16, 'nsew', lambda:self.obj.modificar(self.prod, 
                                                                               self.cant, 
                                                                               self.prec, 
                                                                               self.obj3.tabla))
        
        self.obj2.boton('Devolver', 20, 17, 'nsew', lambda:self.obj.devolver(self.obj3.tabla,
                                                                              self.lista,
                                                                              self.campos))
        
        self.obj2.boton('Stock', 20, 18, 'nsew', lambda:self.obj.seleccionlist(self.obj2.listab))
        
        self.obj2.boton('Lista', 29, 16, 'nsew', lambda:self.obj.obtprod(self.obj2.listab))
        
        self.obj2.boton('Limpiar', 29, 17, 'nsew', lambda:self.obj.camposdel(self.campos))
        
        self.obj2.boton('Salir', 29, 18, 'nsew', self.raiz.quit)
        
        # OBJETO CORRESPONDIENTE A LABEL CON INDICACIONES DE AYUDA
        self.obj2.etiqueta1("BOTONES:"+
                    "\n INGRESO: Alta de elementos"+
                    "\n CONSULTA: Consultar base de datos"+
                    "\n ELIMINAR: Borra elemento seleccionado"+
                    "\n MODIFICACIÓN: Ingresa datos devueltos"+
                    "\n DEVOLVER: Rellena campos para modificarlos"+
                    "\n STOCK: Muestra totales del producto seleccionado"+
                    "\n LISTA: Rellena lista de productos"+
                    "\n LIMPIAR: Limpia campos de ingreso",
                    32, 0, None, 10, 10, 11, 5, 'left') 

        # OBJETOS CORRESPONDIENTES A LOS RADIOBUTTONS
        self.obj2.radiob('Estilo 1', self.opcion, '01', 8, 16, lambda: estilos.estilo1(self, self.raiz,
                                                                                        self.obj8.etiq,
                                                                                        self.obj9.etiq,
                                                                                        self.obj10.etiq,
                                                                                        self.obj2.etiq1))
        
        self.obj2.radiob('Estilo 2', self.opcion, '02', 9, 16, lambda: estilos.estilo2(self, self.raiz,
                                                                                       self.obj8.etiq,
                                                                                       self.obj9.etiq,
                                                                                       self.obj10.etiq,
                                                                                       self.obj2.etiq1))
        
        self.obj2.radiob('Estilo 3', self.opcion, '03', 10, 16, lambda: estilos.estilo3(self, self.raiz,
                                                                                        self.obj8.etiq,
                                                                                        self.obj9.etiq,
                                                                                        self.obj10.etiq,
                                                                                        self.obj2.etiq1))
       
    
    

    