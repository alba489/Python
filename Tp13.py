print("-------------------------------------------------------")
print("Ejercicio13")
print("-------------------------------------------------------")
#Entradas
ano = int( input("Ingrese el Año: "))
#Salida
print("-------------------------------------------------------")
if  ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print("El año es Bisiesto")
else:
    print("El  año no es Bisiesto")