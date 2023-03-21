#Descripcion de Trabajo
import math


print("-------------------------------")
print("Ejercicio 6")
print("-------------------------------")
#Ingreso de datos
AX=int (input("Ingrese las coordenada X de A "))
AY=int (input("Ingrese las coordenada Y de A "))
BX=int (input("Ingrese las coordenada X de B "))
BY=int (input("Ingrese las coordenada Y de B "))
#Proceso
D=((AX-BX)**2+(AY-BY)**2)**0.5
#Solida
print(D)
print ("La distancia es ", D)