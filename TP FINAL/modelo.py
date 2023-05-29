
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

import os
from tkinter import messagebox
from cls.baseorm import Registro 
from cls.baseorm import BasePeewee
from cls.validar import Validar
from decorador import decorador_registro
from observador import Subject

class Modelo(Subject):
    """Clase Modelo.
    Hereda de Subject.
    """
    #CONSTRUCTOR DE LA CLASE MODELO
    def __init__(self,):
        """Constructor de la Clase Modelo.
        
        objdb = Registro ( BasePeewee )
        obja1 = Validar ()
        
        """
        self.objdb = Registro(BasePeewee)
        self.objval=Validar()

    """ A los dferentes métodos se les aplica un decorador, que realizará una acción 
    determinada conforme al método en cuestión.
    
    """
    # BORRA LOS CAMPOS DE LOS ENTRY  
    @decorador_registro  
    def camposdel(self, campos):
        """Método para borrar los campos de los Entry.
        
        Args:
            :campos: datos seleccionados.
            
        """
        for campo in campos:
            campo.set("")
        
          
    # INGRESA LOS REGISTROS A LA BASE DE DATOS Y AL TREEVIEW
   
    @decorador_registro
    def ingresar(self, prod, cant, prec, tabla, campos):
        """Método Ingresar.
        
        Nos permite dar ingreso a nuevos artículos en la base de datos.
        
        Args:
            :prod: productos, del tipo cadena de texto.
            :cant: cantidad, del tipo Integer, números reales.
            :prec: precio, del tipo Integer, n´mero reales.
            :tabla: 
            :campos(_Treeview): Objeto del Treeview.

"""
        self.data_prod = prod.get()
        self.data_cant = cant.get() 
        self.data_prec = prec.get() 
        
        reg=Registro()
        try:
            self.objval.validar_producto(self.data_prod)
            self.objval.validar_cantidad(self.data_cant)
            self.objval.validar_precio(self.data_prec)
            
            reg.prod=prod.get().upper()
            reg.cant=cant.get()
            reg.prec=prec.get()
            reg.save()
            self.actualtabla(tabla)
            
            self.obtdicc()        
            self.camposdel(campos)
            self.notificar(str(self.actualtabla(tabla)), reg.prod, reg.cant, reg.prec)
            messagebox.showinfo('Ingreso',
                                'Datos ingresados exitosamente')
        except:
            messagebox.showerror('Error',
                                 'Datos ingresados incorrectos')
        
        
            
    # ACTUALIZA LO MOSTRADO EN EL TREE VIEW DESDE LA BASE DE DATOS
    def actualtabla(self, tree):
        """Método de actualización del Treeview.
        
        Nos permite actualizar los datos que se muestran en el Treeview
        tomando los registros desde la base de datos.
        
        Args:
            :tree(_Treeview): Objeto del Treeview.
        
        """
        self.registros = tree.get_children()
        for x in self.registros:
            tree.delete(x)
        
        for i in Registro.select():
            tree.insert("", 0, text=i.id, values=(i.prod, i.cant, i.prec))
        return i
    
        
    # BORRA REGISTRO SELECCIONADO EN EL TREEVIEW DE LA BASE DE DATOS
    
    @decorador_registro
    def borrar(self, tabla):
        """Método borrar.
        
        Nos permite borrar el registro seleccionado de la base de datos.
        
        Args:
            :tabla(_Treeview): Objeto del Treeview.

        """
        val = tabla.selection()    
        item = tabla.item(val)
        borra=Registro.get(Registro.id==item['text'])
        borra.delete_instance()
        self.actualtabla(tabla)
        messagebox.showwarning('Borrado', 'Se borró exitosamente')

    # MUESTRA EN EL TREEVIEW LO EXISTENTE EN LA BASE DE DATOS
    @decorador_registro
    def consultar(self, tabla):
        """Método consultar.
        
        Nos deuelve al Treeview los datos existentes en la base de datos.

        Args:
            :tabla(_Treeview): Objeto del Treeview.

        """
        self.actualtabla(tabla)

    # INSERTA EN LOS ENTRY LOS VALORES SELECCIONADOS DESDE EL TREEVIEW
    @decorador_registro    
    def devolver(self, tabla, lista, campos):
        """Método devolver.
        
        Retorna los datos seleccionados en el Treeview a los Entry,
        para su posterior modificación o actualización.

        Args:
            :tabla(_Treeview): Objeto del Treeview.
            :lista: lista de elementos.
            :campos(_Treeview): Objeto del Treeview.
        
        En caso de producirse un error al no seleccionar elementos
        desde el Treeview, se decuelve un mensaje de error mediante un
        messagebox.

        """
        val = tabla.selection()
        item = tabla.item(val)['values']

        try:
           for i in range(len(lista)):
               lista[i] = campos[i].set(item[i])
               
        except:
            messagebox.showerror('ERROR', 'Por favor, debe realizar una selección')

    # MODIFICA LOS VALORES EN LA BASE DE DATOS DESDE LOS ENTRY        
    @decorador_registro
    def modificar(self, prod, cant, prec, tabla):
        """Método modificar.
        
        Permite realizar la modificación de los datos existntes en la 
        base de datos.
        
        Args:
            :prod: productos, del tipo cadena de texto.
            :cant: cantidad, del tipo Integer, números reales.
            :prec: precio, del tipo Integer, números reales.
            :tabla(_Treeview): Objeto del Treeview.
            
        """
        val = tabla.selection()
        item = tabla.item(val)
        actualiza=Registro.update(prod=prod.get(),
                                  cant=cant.get(),
                                  prec=prec.get()).where(Registro.id==item['text'])
        actualiza.execute()
        self.actualtabla(tabla)
        messagebox.showinfo('Modificar', 'Se actualizó registro')


    # OBTIENE LOS REGISTROS DE LA BASE DE DATOS EN FORMATO DICCIONARIO
    def obtdicc(self):
        """Método Obtención diccionario.
        
        Nos permite obtener los registros de la base de datos 
        en formato de diccionario.
        
        """
        resultado = []
        query = Registro.select().dicts()
        for row in query:
                resultado.append(row)
        return resultado

    # SE INSERTA EN LISTBOX LOS DATOS DE LA COLUMNA PROD DE LA BASE DE DATOS
    @decorador_registro
    def obtprod(self, listab):
        """Método Obtención productos.
        
        Nos permite insertar en el Listbox los datos obrantes en la Columna
        "Producto" en la base de datos.
        Relizamos una conslta y una "extracción" de datos.
        
        """
        listab.delete(0, 'end')
        query = Registro.select()
        lista = []
        
        for fila in query:
            lista.append((fila.prod).upper())
            lista.sort()
        for i in lista:
            listab.insert('end', i)
        
        
    # SE SELECCIONA UN PRODUCTO EN LISTBOX PARA BUSCAR Y SE RECIBE LOS DATOS DE STOCK (CANTIDAD Y VALOR) 
    @decorador_registro        
    def seleccionlist(self, listab):
        """Método Selección Lista.
        
        Se selecciona un producto desde el Listbox y esto nos permite buscar
        y recibir los datos referentes a la cantidad y el valor del producto
        determinado conforme a su stock en la base de datos.

        En caso de producirse un error al no seleccionar elementos
        desde el Listbox, se decuelve un mensaje de error mediante un
        messagebox.
        
        """
        sub = []
        compra = self.obtdicc()
        busqueda = 0
    
        for i in listab.curselection():
            tupla =listab.get(i)
            busqueda = tupla
            
            for x in compra:
                if busqueda == x['prod'].upper():
                    consulta = x
                    sub.append(consulta)
               
        if busqueda == 0:
            messagebox.showerror('ERROR', 'Por favor, ingrese una busqueda válida')
                
        cantidadlist = []
        preciolist = []
        subtotallist = []
        
        for item in sub:
            cantidadlist.append(item['cant'])
            preciolist.append(item['prec'])
            subtotallist.append(item['cant']*item['prec'])

        cantidad = sum(cantidadlist)
        
        subtotal = sum(subtotallist)

        info = "El Stock de " + str(busqueda) + " es de "+ str(cantidad) + " y su valor es de " + str(subtotal)
        messagebox.showinfo('STOCK', info)      

    # MUESTRA POR MEDIO DE UN MESSAGEBOX EL TOTAL DEL VALOR DE TODOS LOS PRODUCTOS DESDE EL DICCIONARIO
    @decorador_registro           
    def totalinfor(self):
        """Método Información Total.
        
        Muestra por medio de un Messagebox el total del valos de todos los productos
        obtenidos desde el diccionario creado.
        
        """
        totallist = []
        compra = self.obtdicc()
        for j in compra:
            totallist.append(j['cant']*j['prec'])
            
        total = sum(totallist)
        totalinfo = "El Total de Stock es de " + str(total)
        messagebox.showinfo('STOCK', totalinfo)

    # ABRE EL ARCHIVO PDF DE AYUDA INCLUIDO
    @decorador_registro
    def ayuda(self):
        """Método ayuda.
        
        Nos de acceso al archivo en formato *pdf donde se encuentra
        el Manual de Ayuda sobre el uso de la aplicación.
        
        """
        ruta = 'ayuda.pdf'
        os.system(ruta)
        
        
    def datos_stats(self,):
        x = self.obtdicc()
        return x


        