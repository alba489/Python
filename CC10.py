print("-------------------------------------------------------")
print("Complemento 10")
print("-------------------------------------------------------")
#Entradas
ca = 0
numCar = 10
print("Ingrese", numCar, "caracteres: ")
#Proceso
for i in range(0, numCar):
    m = input("Ingrese Caracter: ")
    if m == "a" :
        ca = ca + 1
#Salida
print ("En", numCar, "caracteres hay", ca, "caracteres 'a'")