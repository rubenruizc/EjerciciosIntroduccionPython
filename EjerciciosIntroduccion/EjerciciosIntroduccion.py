#coding: latin1
#Ejercicio 09
#Escribe una función a la que se le pasen dos enteros y muestre 
#todos los números comprendidos entre ellos. 
#Desde el método main() lee los dos números enteros, los cuales deben 
#introducirlos el usuario, y pásalos como parámetros de entrada de la función.
def funcion (parametro1,parametro2):
    for contador in range (parametro1 + 1,parametro2):
        print(contador, end = " ")
    return

def main():
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))
    
    while(num1 == num2):
        print("Los dos números son iguales")
        num2 = int(input("Dime otro número: "))
    print("Los números entre " + str(num1) + " y " + str(num2) + " son: ", end = " ")
    funcion(num1 if (num1 < num2) else num2, num2 if (num2>num1) else num1)

if __name__ == "__main__":
    main()




