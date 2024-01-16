#Ejercicio 2: Dadas dos variables numéricas A y B, que el usuario debe introducir por consola, se
#pide realizar un algoritmo que intercambie los valores de ambas variables y muestre por pantalla
#cuanto valen al final las dos variables

A= int(input("Valor de la variable A " ))
B= int(input("Valor de la variable B" )) 
print (A)
print (B)
aux=A
A=B
B=aux
print("El valor de A es ", A, "el valor de B es " , B)
