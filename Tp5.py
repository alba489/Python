#Descripcion de Trabajo
import math


print("-------------------------------")
print("Ejercicio 5")
print("-------------------------------")
#Ingreso de datos
GB=int (input("Ingrese numero de Gigabyte del Disco Duro "))
#Proceso
MG=GB*1024;
MD=MG/1.44;
#Solida
print(MD)
print ("Numero de Discos necesarios ", math.ceil(MD))