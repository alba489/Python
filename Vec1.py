print("-------------------------------------------------------")
print("Vector 1")
print("-------------------------------------------------------")
#Entradas
i = 1
F=[]
#Proceso
print("Ingrese el numero de elementos: ")
numElementos= int(input())
while i <= numElementos :
    elemento = int( input("Ingrese Elemento: "))
    F.append(elemento) 
    i=i+1
#Salida
print (F)