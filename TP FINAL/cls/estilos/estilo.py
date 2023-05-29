# TRABAJO PRACTICO FINAL NIVEL INTERMEDIO, DIPLOMATURA DE PYTHON
# REALIZADO POR PAMELA MORSENTTI Y FRANCISCO PRADO, CURASADA #999188625

# CLASE PARA DAR DIFERENTES ESTILOS


class estilos:
    """Clase estilos

    Determina los diferentes estilos con que se puede configurar
    la aplicaciòn.

    """

    def estilo1(self, raiz, etiq, etiqu, etique, etiq1):
        self.raiz = raiz
        self.etiq = etiq
        self.etiqu = etiqu
        self.etique = etique
        self.etiq1 = etiq1
        self.estilo_1 = "#D1EDF0"
        self.raiz.configure(bg=self.estilo_1)
        self.etiq.configure(bg=self.estilo_1)
        self.etiqu.configure(bg=self.estilo_1)
        self.etique.configure(bg=self.estilo_1)
        self.etiq1.configure(bg=self.estilo_1)
        return self.raiz

    def estilo2(self, raiz, etiq, etiqu, etique, etiq1):
        self.raiz = raiz
        self.etiq = etiq
        self.etiqu = etiqu
        self.etique = etique
        self.etiq1 = etiq1
        self.estilo_2 = "#F5EE60"
        self.raiz.configure(bg=self.estilo_2)
        self.etiq.configure(bg=self.estilo_2)
        self.etiqu.configure(bg=self.estilo_2)
        self.etique.configure(bg=self.estilo_2)
        self.etiq1.configure(bg=self.estilo_2)
        return self.raiz

    def estilo3(self, raiz, etiq, etiqu, etique, etiq1):
        self.raiz = raiz
        self.etiq = etiq
        self.etiqu = etiqu
        self.etique = etique
        self.etiq1 = etiq1
        self.estilo_3 = "#AFFF33"
        self.raiz.configure(bg=self.estilo_3)
        self.etiq.configure(bg=self.estilo_3)
        self.etiqu.configure(bg=self.estilo_3)
        self.etique.configure(bg=self.estilo_3)
        self.etiq1.configure(bg=self.estilo_3)
        return self.raiz
