print("-------------------------------------------------------")
print("Ejercicio4")
print("-------------------------------------------------------")
#Constante
num= int(input("Ingrese un Numero: "))
#Proceso
while num>0:
    Resto= num%10
    num = num // 10
    #Salida
    print(Resto)
