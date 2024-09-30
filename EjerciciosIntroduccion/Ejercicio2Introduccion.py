#coding: latin1
#Ejercicio 2
#Pedir dos números y mostrarlos ordenados de menor a mayor.

num1 = int (input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

if(num1 > num2):
    resultado = str(num1) + " > " + str(num2)
elif (num2 > num1) :
    resultado = str(num2) + " > " + str(num1)
else :
    resultado = str(num1) + " = " + str(num2)

print (resultado)