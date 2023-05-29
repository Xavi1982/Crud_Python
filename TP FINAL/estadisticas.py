
# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

import pandas as pd
import matplotlib.pyplot as plt
from modelo import Modelo

class Estadisticas:
    """ Clase Estadísticas.
    
    Nos premitirá generar estadísticas basadas en los ingresos en la base de datos
    de los productos, sus valores y sus cantidades.
    
    Establecemos el objeto de la Clase Moldelo().
    
    """
    obj= Modelo()
    datos = obj.datos_stats()
    df = pd.DataFrame(datos, columns=['prod', 'cant', 'prec'])
    df['subt'] = df['cant']*df['prec'] 
    df = df.set_index('prod')
    df1 = df.groupby(['prod'])[['cant','subt']].sum()
    plt.rcParams.update({'font.size': 8})
    
    def mayor_cant(self):
        """ Método que determinará los 5 productos con mayor cantidad.

        """
        plt.figure(figsize=(12,6))
        s1 = self.df1['cant'].nlargest()
        s1 = s1.sort_values()
        colores=['yellow','orange', 'orangered', 'red', 'darkred']
        plt.barh(s1.index, s1, color=colores)
        plt.title('TOP 5, Productos medidos por cantidad')
        plt.xlabel('Cantidad')
        plt.ylabel('Producto')
        plt.show()

    def mas_caro(self):    
        """ Método para determinar los 5 productos más caros.

        """
        plt.figure(figsize=(12,6))
        s2 = self.df['prec'].nlargest()
        s2 = s2.sort_values()
        colores=['yellow','orange', 'orangered', 'red', 'darkred']
        plt.barh(s2.index, s2, color=colores)
        plt.title('TOP 5, Productos medidos por precio')
        plt.xlabel('Precio')
        plt.ylabel('Producto')
        plt.show()

    def mayor_gasto(self,):
        """Método para determinar los 5 productos con mayor gasto.
        
        """
        plt.figure(figsize=(12,6))
        s3 = self.df1['subt'].nlargest()
        s3 = s3.sort_values()
        colores=['yellow','orange', 'orangered', 'red', 'darkred']
        plt.barh(s3.index, s3, color=colores)
        plt.title('TOP 5, Mayor gasto por producto')
        plt.xlabel('Subtotal')
        plt.ylabel('Producto')
        plt.show()

