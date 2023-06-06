print("-------------------------------------------------------")
print("Complemento 8")
print("-------------------------------------------------------")
#Entradas
n = int( input("Ingrese la cantidad de números a evaluar: "))
c = 0
#Proceso
for i in range(1, n+1):
    num = int( input("Ingrese número: "))
    if num == 0 :
        c = c+1
#Salida
print ("Hay ", c, " números ceros")
