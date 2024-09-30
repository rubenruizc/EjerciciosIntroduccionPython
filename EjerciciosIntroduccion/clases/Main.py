#coding: latin1
from clases.EjercicioClase import Calculo

num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

cal = Calculo(num1,num2)

def main():
    print("Suma: " + str(cal.suma()))
    print("Resta: " + str(cal.resta()))
    print("Multiplicación: " + str(cal.multiplicacion()))
    print("División: " + str(cal.division()))

if __name__ == "__main__":
    main()