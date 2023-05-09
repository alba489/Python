print("-------------------------------------------------------")
print("Ejercicio1")
print("-------------------------------------------------------")
#Entrada
C=-1
I=0
T=0
while (C<0) or (I<=0) or (I>=100) or (T<=0):
    print ("Introduce el capital, el interés y el tiempo apropiados")
    C= int(input("Capital: "))
    I= int(input("Interes: "))
    T= int(input("Tiempo en Años: "))
#Proceso
for i in range (T):
    C=C*(1+I/100)
    i=i+1
#Salida
print ("Tienes", C , "soles")