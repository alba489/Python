print("-------------------------------------------------------")
print("Ejercicio2")
print("-------------------------------------------------------")
#Entrada
print ("Introduce el capital, el interés y el tiempo apropiados")
num= int(input("Numeros: "))
suma=0
i=1
#Proceso
while num>0:
    for i in range (1,+num+1):
        if num % i == 0:
            suma=suma+i

        i=i+1    
    #Salida
    print("La suma de los divisores del número es: ", suma)
    suma=0
    num = int( input("Núm: "))   
