#coding: latin1
#Codificar el juego “el número secreto”, 
#que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
#Para ello se introduce por teclado una serie de números, para los que se indica: 
#“mayor” o “menor”, según sea mayor o menor con respecto al número secreto. 
#El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).
import random


random = random.randint(1,100)
print (random)
num = int(input("Introduzca un número: "))

while(num != random and num !=-1):
    
    print("Menor" if (num < random) else "Mayor")
    num = int(input("Introduzca un número: "))

print("Enhorabuena eres igual de listo que Amaro" if (num != -1) else ("Te rendiste"))
