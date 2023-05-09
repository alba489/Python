print("-------------------------------------------------------")
print("Complementario 1")
print("-------------------------------------------------------")
#Constante
c=0
#Proceso
print("Ingrese 10 numeros: ")
for i in range(1, 10 + 1):
    num = int( input("Ingrese Número: "))
    if num % 2 == 0 :
        c = c + 1
#Salida
print("Hay", c, "números pares")