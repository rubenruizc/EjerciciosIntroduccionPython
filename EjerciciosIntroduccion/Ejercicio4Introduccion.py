#coding: latin1
#Codificar el juego �el n�mero secreto�, 
#que consiste en acertar un n�mero entre 1 y 100 (generado aleatoriamente). 
#Para ello se introduce por teclado una serie de n�meros, para los que se indica: 
#�mayor� o �menor�, seg�n sea mayor o menor con respecto al n�mero secreto. 
#El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).
import random


random = random.randint(1,100)
print (random)
num = int(input("Introduzca un n�mero: "))

while(num != random and num !=-1):
    
    print("Menor" if (num < random) else "Mayor")
    num = int(input("Introduzca un n�mero: "))

print("Enhorabuena eres igual de listo que Amaro" if (num != -1) else ("Te rendiste"))
