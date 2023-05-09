print("-------------------------------------------------------")
print("Complementario 5")
print("-------------------------------------------------------")
#Constante
n = int( input("Ingrese el número de términos: "))
s = 0
ser = 0
#Proceso
#Proceso
for a in range(1,n+1):
    if (a%2 == 0):
        s=s-(1/a)
    else:
        s=s+(1/a)
#Salida
print("La suma de la serie: ", s)