print("-------------------------------------------------------")
print("Complemento 11")
print("-------------------------------------------------------")
#Entradas
c = 0
i = 1
NE = 10
#Proceso
print("Ingrese", NE, "Números:")
while i <= NE:
    num = int( input("Ingrese número: "))
    if n%2 == 0 :
        c = c + 1
    i = i + 1
#Salida
print ("En", NE, "números enteros hay", c, "números pares")