
class Padre():
    def __init__(self,nombre):
        self.nombre = nombre

    def saludo(self):
        print("Hola, soy el padre, ", self.nombre)

class Hija (Padre):
    def __init__(self,nombre,padre):
        super().__init__(nombre)
        self.padre = padre

    def saludo(self):
        print("Hola, soy la hija, " + self.nombre + " y mi padre es " + self.padre.nombre)
