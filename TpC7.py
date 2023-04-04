#Descripcion de Trabajo
import math
print("-------------------------------")
print("Ejercicio Complementario 7")
print("-------------------------------")
#Constante
PI=3.1416
#Ingreso de datos
b=int (input("Ingrese el primer lado "))
c=int (input("Ingrese el segundo lado "))
alfa=float (input("Ingrese el ángulo en grados sexagesimales "))
#Proceso
a=(b**2 +c**2-2*b*c*math.cos(alfa*PI/180))**0.50
#Solida
print("El lado a es:", a)