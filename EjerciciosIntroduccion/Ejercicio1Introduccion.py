#coding: latin1
#Ejercicio 1
#Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

num = int(input("Introduzca un número: "))

if(num % 2 == 0):
    resultado = "par"
else :
    resultado = "impar"

print("El número " + str(num) + " es: " + str(resultado))