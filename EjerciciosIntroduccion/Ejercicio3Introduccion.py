#coding: latin1
#Ejercicio 3
#Escribe un programa que vaya pidiendo al usuario n�meros enteros positivos 
#que debe ir sumando. Cuando el usuario no 
#quiera insertar m�s n�meros, introducir� un n�mero negativo y el algoritmo, 
#antes de acabar, mostrar� la suma de los n�meros positivos introducidos por el usuario.

sum = 0
num = int(input("Introduzca un n�mero: "))
while(num > 0):
    sum += num
    num = int(input("Introduzca un n�mero: "))

print(sum)