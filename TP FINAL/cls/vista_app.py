
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

from tkinter import Scrollbar
from tkinter import Listbox
from tkinter import ttk
from tkinter import Label
from tkinter import Menu
from tkinter import Entry
from modelo import Modelo
from estadisticas import Estadisticas
from cls.servidor import Server

# CLASE VISTAAPP DEFINE CADA UNO DE LOS ELEMENTOS DE LA VISTA DE TKINTER

class VistaApp():
    """Clase VistaApp."""

    #CONSTRUCTOR DE LA CLASE VISTAAPP
    def __init__(self, raiz,):
        """Constrctor de la clase VistaApp.
        
        Args:
            :raiz: Ventana raíz de la aplicación
                    (Interfaz gráfica del usuario).

            """
        
        self.raiz = raiz
        self.raiz.title("Proyecto")
        self.raiz.geometry("1020x680")
        combo = ttk.Combobox(self.raiz)
        self.combo = combo
        listab = Listbox(self.raiz)
        self.listab = listab
        scrol = Scrollbar(self.raiz)
        self.scrol = scrol
        tabla = ttk.Treeview(self.raiz)
        self.tabla = tabla        
        barra_menu = Menu(self.raiz, )
        self.barra_menu = barra_menu
        self.obj = Modelo()
        self.obje = Estadisticas()
        self.objs = Server()
    
    # FUNCIóN PARA CREAR LABELS
    def etiqueta(self, text, row, column, sticky=None):
        """Método para la creación de las etiquetas.

        Args:
            :text = text, texto
            :row = row, fila
            :column = column, columna
            :sticky = sticky = None. Permite establecer la posición del elemento.

        """
        self.text = text
        self.row = row
        self.column = column
        self.sticky = sticky
        
        self.etiq = Label(self.raiz,
                          text=self.text)    
        self.etiq.grid(row=self.row, column=self.column,
                       sticky=self.sticky)
    
    # FUNCIóN PARA CREAR LABEL DE AYUDA
    
    def etiqueta1(self, text, row, column, sticky,
                  height, rowspan, columnspan, padx, justify):
        """Método para la creación de las etiquetas de ayuda.

        Args:
            :text = text, texto
            :row = row, fila
            :column = column, columna
            :sticky = sticky, permite establecer la posición del elemento.
            :height = height, altura
            :rowspan = rowspan, indica la cantidad de filas que ocupará la celda.
            :columnspan = columnspan, indica la cantidad de columnas que debe ocupar la celda.
            :padx = padx, indica los másgenes del elemento.
            :justify = justify, permite establecer la justificación del elemento.

        """

        self.text = text
        self.row = row
        self.column = column
        self.sticky = sticky
        self.height = height
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.padx = padx
        self.justify = justify
        
        self.etiq1 = Label(self.raiz,
                           text=self.text)
        self.etiq1.grid(row=self.row, column=self.column,
                        sticky=self.sticky)
    
    # FUNCIóN PARA CREAR ENTRIES    
    def caja(self, width, var, row, column, columnspan, sticky, ipady):
        """Método para la creación de los "entries" o cajas de toma de datos.

        Args:
            :widht = width, ancho
            :var = variable
            :row = row, fila
            :column = column, columna
            :columnspan = columnspan, indica la cantidad de columnas que debe ocupar la celda.
            :sticky = sticky, permite establecer la posición del elemento.
            :ipady = ipady, indica los másgenes del elemento.
        
        """
        self.width=width
        self.var=var
        self.row=row
        self.column=column
        self.columnspan=columnspan
        self.sticky=sticky
        self.ipady=ipady
        
        self.caj=Entry(self.raiz, width=self.width, textvariable=self.var)
        self.caj.grid(row=self.row, column=self.column,
                      columnspan=self.columnspan,
                      sticky=self.sticky, ipady=self.ipady)
        self.caj.delete(0, 'end')
    
    # FUNCIóN PARA CREAR BOTONES
    def boton(self, text, row, column, sticky, command):
        """Método para la creación de los botones.

        Args:
            :text = text, texto
            :row = row, fila
            :column = column, columna
            :sticky = sticky, permite establecer la posición del elemento.
            :command = indicará la función que realizará cada botón.

        """
        self.text=text
        self.row=row
        self.column=column
        self.sticky=sticky
        self.command=command
        
        self.boto=ttk.Button(self.raiz,
                             text=self.text,
                             command=self.command)
        self.boto.grid(row=self.row, column=self.column, sticky=self.sticky)
    
    # FUNCIóN PARA CREAR LISTBOX Y SU SCROLLBAR
    def lista(self):
        """Método para la cración del Listbox y Scrollbar.

        """
        self.listab = Listbox(self.raiz, height=28, selectmode='extended')
        self.listab.grid(column=0,row=1, rowspan=26, columnspan=6, sticky='nsew')
        
        self.scrollista = Scrollbar(self.raiz,orient='vertical',command=self.listab.yview)
        self.scrollista.grid(column=7, row=1, rowspan=26, sticky='ns')
    
    # FUNCIóN PARA CREAR TREEVIEW Y SU SCROLLBAR        
    def tablap(self):
        """Método para la creaciòn del Treeview y Scrollbar.

        """
        self.tabla['columns'] = ('Producto','Cantidad','Precio')

        self.tabla.column('#0', width=50, minwidth=30, anchor='w')
        self.tabla.column('Producto', width=150, minwidth=100, anchor='w')
        self.tabla.column('Cantidad', width=100, minwidth=80, anchor='w')
        self.tabla.column('Precio', width=90, minwidth=70, anchor='w')

        self.tabla.heading('#0', text='ID', anchor='center')
        self.tabla.heading('Producto', text='Producto', anchor='center')
        self.tabla.heading('Cantidad', text='Cantidad', anchor='center')
        self.tabla.heading('Precio', text='Precio', anchor='center')
        self.tabla.grid(column=8,row=1, columnspan=4, rowspan=26, sticky='nsew')
        
        self.scroltabla = Scrollbar(self.raiz, orient='vertical', command=self.tabla.yview)
        self.scroltabla.grid(column=13, row=1, rowspan=26, sticky='ns')
    
    # FUNCIóN PARA CREAR MENU   
    def menu(self,):
        """Método para la creación del Menú.
        
        Se genera el Menú desplegable que presenta las siguientes opciones:
        1- Ayuda
        2- Total
        3- Estadísticas
           3-1 Top 5 Cantidades
           3-2 Top 5 Precios
           3-3 Top 5 Gastos
        4- Servidor
            4-1 Servidor ON
            4-2 Servidor OFF
        5-  Salir.
        
        """
        self.menu_opciones = Menu(self.barra_menu, tearoff=0)
        self.menu_opciones.add_command(label="Ayuda", command=lambda:self.obj.ayuda())
        self.menu_opciones.add_command(label="Total", command=lambda:self.obj.totalinfor())
        self.sub_menu = Menu(self.barra_menu, tearoff=0)
        self.sub_menu.add_command(label="Top 5 Cantidades", command=lambda:self.obje.mayor_cant())
        self.sub_menu.add_command(label="Top 5 Precios", command=lambda:self.obje.mas_caro())
        self.sub_menu.add_command(label="Top 5 Gastos", command=lambda:self.obje.mayor_gasto())
        self.menu_opciones.add_cascade(label="Estadísticas", menu=self.sub_menu)
        self.sub_menu1 = Menu(self.barra_menu, tearoff=0)
        self.sub_menu1.add_command(label="Servidor ON", command=lambda:self.objs.try_connection())
        self.sub_menu1.add_command(label="Servidor OFF", command=lambda:self.objs.stop_server())
        self.menu_opciones.add_cascade(label="Servidor", menu=self.sub_menu1)
        self.menu_opciones.add_command(label="Salir", command=self.raiz.quit)
        self.barra_menu.add_cascade(label="Opciones", menu=self.menu_opciones)
        self.raiz.config(menu=self.barra_menu)

    # FUNCIóN PARA CREAR RADIOBUTTONS
    def radiob(self, text, variable, value, row, column, command):
        """Método para la creación de los rediobuttons.

        Args:
            :text = text, texto
            :variable = variable
            :value = value, valor
            :row = row, fila
            :column = column, columna
            :command = indicará la función que realizará cada botón.

        """
        self.text = text
        self.variable = variable
        self.value = value
        self.command = command
        self.row = row
        self.column = column
        
        self.radio = ttk.Radiobutton(self.raiz, 
                                     text=self.text,
                                     variable=self.variable,
                                     value=self.value, 
                                     command=self.command)
        self.radio.grid(row=self.row, column=self.column)
        