#coding: latin1
#Ejercicio 5
#Escribir una aplicaci�n para aprender a contar, 
#que pedir� un n�mero n y mostrar� todos los n�meros del 1 al n

print("Vamos a aprender a contar")
num = int(input("Introduzca un n�mero: "))

while(num < -1) :
    num = int(input("Introduzca un n�mero: "))

for contador in range(1,num + 1) :
    print(contador, end = " ")