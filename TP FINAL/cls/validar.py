
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

import re
from tkinter import messagebox

# CLASE VALIDAR, REALIZA LA VERIFICACIóN Y VALIDACIóN DE DATOS
class Validar:
    """Clase Validar.

    Nos permite realizar los controles de validación.
    Regex: Regular expresion o Expresiones regulares.

    """
    # CONSTRUCTOR DE CLASE VALIDAR
    def __init__(self):
        """Constructor de la clase Validar.
        
        """
        self.val_prod = "^[A-Za-záéíóúÁÉÍÓÚÜüñÑ\s]*$"
        self.val_cant = "^[0-9]+([.][0-9]+)?$"
        self.val_prec = "^[0-9]+([.][0-9]+)?$"
        
    # FUNCIóN PARA VALIDAR PRODUCTO
    def validar_producto(self, prod):
        """Validación de producto.
        
        Args:
            :prod: producto.
            :type: se espera el ingreso de una cadena de texto.
        
        Returns:
            :Devuslve un mensaje de error en caso de no ser correcto el valor ingresado
            o de encontrarse vacío.
        
        """
       
        if len(prod) == 0:
            messagebox.showerror('Error', 
                                 'Debe ingresar un producto')
            raise TypeError
        else:
            
            if re.match(self.val_prod, prod):
                return prod
            else:
                messagebox.showerror('Error',
                                     'Ingrese Producto válido')
            raise TypeError 
          
    # FUNCIóN PARA VALIDAR CANTIDAD       
    def validar_cantidad(self, cant):
        """Validación de cantidad.
        
        Args:
            :cant: cantidad.
            :type: integer. Se espera el ingreso de un número real.
        
        Returns:
            :Devuslve un mensaje de error en caso de no ser correcto el valor ingresado
            o de encontrarse vacío.

        """
        
        if len(cant) == 0:
            messagebox.showerror('Error',
                                 'Debe ingresar una cantidad')
            raise TypeError
        else:
            
            if re.match(self.val_cant, cant):
                return cant
            else:
                messagebox.showerror('Error',
                                        'Ingrese Cantidad válida')
                raise TypeError
            
    # FUNCIóN PARA VALIDAR PRECIO       
    def validar_precio(self, prec):
        """Validación de precio.
        
        Args:
            :prec: precio.
            :type: integer. Se espera el ingreso de un número real.
        
        Returns:
            :Devuslve un mensaje de error en caso de no ser correcto el valor ingresado
            o de encontrarse vacío.

        """

        
        if len(prec) == 0:
            messagebox.showerror('Error',
                                 'Debe ingresar un precio')
            raise TypeError
        else:
            
            if re.match(self.val_prec, prec):
                return prec
            else:
                messagebox.showerror('Error',
                                     'Ingrese un Precio válido')
                raise TypeError            
    

    
    