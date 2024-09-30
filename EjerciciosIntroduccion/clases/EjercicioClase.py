
class Calculo:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    
    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1-self.num2

    def multiplicacion(self):
        return self.num1*self.num2

    def division (self):
        if(self.num2 == 0):
            print("No se puede dividir entre 0")
        else:
            return self.num1/self.num2
