#coding: latin1
#Ejercicio 09
#Escribe una funci�n a la que se le pasen dos enteros y muestre 
#todos los n�meros comprendidos entre ellos. 
#Desde el m�todo main() lee los dos n�meros enteros, los cuales deben 
#introducirlos el usuario, y p�salos como par�metros de entrada de la funci�n.
def funcion (parametro1,parametro2):
    for contador in range (parametro1 + 1,parametro2):
        print(contador, end = " ")
    return

def main():
    num1 = int(input("Introduzca el primer n�mero: "))
    num2 = int(input("Introduzca el segundo n�mero: "))
    
    while(num1 == num2):
        print("Los dos n�meros son iguales")
        num2 = int(input("Dime otro n�mero: "))
    print("Los n�meros entre " + str(num1) + " y " + str(num2) + " son: ", end = " ")
    funcion(num1 if (num1 < num2) else num2, num2 if (num2>num1) else num1)

if __name__ == "__main__":
    main()




