print("-------------------------------------------------------")
print("Complemento 7")
print("-------------------------------------------------------")
#Entradas
n = int( input("Ingrese un número: "))
con = 0
#Proceso
for i in range(2, n):
    if n % i == 0 :
        con = con + 1
#Salida
if con == 0:
    print (n, " Es un número primo")
else:
    print (n, " No es un número primo")