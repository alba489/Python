print("-------------------------------------------------------")
print("Complemento 9")
print("-------------------------------------------------------")
#Entradas
lim = int( input("Ingrese la cantidad de números a comparar: "))
n = int( input("Ingrese un número: "))
#Proceso
men = n
may = n
for i in range(1, lim):
    n = int( input("Ingrese número: "))
    if n < men :
        men = n
    else:
        if n > may :
            may = n
#Salida
print ("El número menor es :" ,men)
print ("El número mayor es :", may)