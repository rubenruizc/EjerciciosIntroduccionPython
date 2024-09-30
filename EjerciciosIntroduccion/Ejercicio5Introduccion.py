#coding: latin1
#Ejercicio 5
#Escribir una aplicación para aprender a contar, 
#que pedirá un número n y mostrará todos los números del 1 al n

print("Vamos a aprender a contar")
num = int(input("Introduzca un número: "))

while(num < -1) :
    num = int(input("Introduzca un número: "))

for contador in range(1,num + 1) :
    print(contador, end = " ")