#coding: latin1
#Ejercicio 1
#Dise�ar una aplicaci�n que solicite al usuario un n�mero e indique si es par o impar.

num = int(input("Introduzca un n�mero: "))

if(num % 2 == 0):
    resultado = "par"
else :
    resultado = "impar"

print("El n�mero " + str(num) + " es: " + str(resultado))