#coding: latin1


triple = """primera línea
                        esto se verá en otra línea"""
print(triple)
#--------------------------------------------------
#Concatenar cadenas
a = "uno"
b = "dos"
c = a+b
print (c)
c = a*3
print (c)
print("\n")
#--------------------------------------------------
#Solo el espacio 5
cadena = "ejemplo de cadena larga"
print(cadena[5])
cadena = "ejemplo de cadena larga"
#Desde el 5 hasta el 15
print (cadena [5:15])
print("\n")
#--------------------------------------------------
#Separar palabras de una cadena
cadena = "ejemplo de cadena larga"
palabras = cadena.split()
print(palabras)

#Cada vez que encuentra una e rompe la cadena y la mete en el array
palabras = cadena.split('e')
print (palabras)
print("\n")
#--------------------------------------------------
#Juntar palabras para formar una cadena
cadena = " ".join(['cadena','con','varias','palabras'])
print(cadena)
print("\n")
#--------------------------------------------------
#if,elif,else
numero = -4
if numero < 0 :
    print("negativo")
elif numero > 0:
    print("positivo")
else :
    print("cero")
print("\n")
#--------------------------------------------------
#Ternario
num = 3
var = "par" if (num%2 == 0) else "impar"
print (var)
print("\n")
#--------------------------------------------------
#Bucle for
cadena = input ("Introduce una cadena : ")
for letra in cadena:   
    print(letra, end = " ")

print ("\n")

#Cuenta hasta 100
for contador in range(1,101) :
    print(contador, end = " ")

print ("\n")

#--------------------------------------------------
#Funciones
def mi_funcion (param1,param2):
    """ suma los parámetros de entrada y
    devuelve el resultado """
    res = param1 + param2
    return res
suma = mi_funcion(3,2)
print ("La suma es: " + str(suma))

print("\n")

#--------------------------------------------------
edad = int(input("Dime tu edad: "))
doble = edad*2
print ("Tienes " + str(edad) + " años y el doble sería " + str(doble))