#Descripcion de Trabajo
import math
print("-------------------------------")
print("Ejercicio Complementario 10")
print("-------------------------------")
#Ingreso de datos
print("Ingrese los valores de los punto A. x1, y1, z1 ")
x1=float( input("x1: "))
y1=float( input("y1: "))
z1=float( input("z1: "))
print("Ingrese los valores de los puntos B. x2, y2, z2 ")
x2=float( input("x2: "))
y2=float( input("y2: "))
z2=float( input("z2: "))
#Proceso
dis=((z2-z1)**2+(y2-y1)**2+(x2-x1)**2)**0.5
#Solida
print("La distancia es: ",dis)