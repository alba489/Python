print("-------------------------------------------------------")
print("Vector 2")
print("-------------------------------------------------------")
#Entradas
Suma=0
Media=0.0
C=0
Temp=[]
#Proceso
print("Ingrese la cantidad de temperatura: ")
N= int(input())
for i in range (N):
    temperatura = float(input("Ingrese la Temperatura {0}:".format(i + 1)))
    Temp.append(temperatura)
    Suma=Suma+Temp[i]
Media=Suma/N
for tempElement in Temp:
    if tempElement>=Media:
        C=C+1
        print(tempElement)
#Salida
print ("La media es ", Media)
print ("Total de temperatura >= a la media es ", C)