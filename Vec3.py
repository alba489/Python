print("-------------------------------------------------------")
print("Vector 3")
print("-------------------------------------------------------")
#Entradas
Vec=[]
#Proceso
print("Ingrese el numero de elementos: ")
N= int(input())
if 1<=N and N<=200:
    for i in range (1,N+1):
        elemento = float(input("Ingrese Entero {0}:".format(i)))
        Vec.append(elemento)
    i=0
    Nuevo=[]
    for elemento in Vec:
        if elemento not in Nuevo:
            Nuevo.append(elemento)
    Nuevo.sort()
#Salida
print (Nuevo)