#coding: latin1
from clases.EjercicioClase import Calculo

num1 = int(input("Introduzca un n�mero: "))
num2 = int(input("Introduzca otro n�mero: "))

cal = Calculo(num1,num2)

def main():
    print("Suma: " + str(cal.suma()))
    print("Resta: " + str(cal.resta()))
    print("Multiplicaci�n: " + str(cal.multiplicacion()))
    print("Divisi�n: " + str(cal.division()))

if __name__ == "__main__":
    main()