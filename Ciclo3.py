print("-------------------------------------------------------")
print("Ejercicio3")
print("-------------------------------------------------------")
#Constante
primero = 2
limete = 1000
Cont=0
#Proceso
for i in range (primero, limete):
    primo= True
    j=2
    while (i > j) and (primo == True):
        if i%j == 0 :
            primo=False
            break
        else:
            j=j+1
    if primo == True :
        print(i, "es primo.")
        Cont = Cont + 1
#Salida
print("Entre", primero, "y" , limite, "hay", Cont, "nº primos")
