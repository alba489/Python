print("-------------------------------------------------------")
print("Complementario 6")
print("-------------------------------------------------------")
#Entradas
print("Ingrese los 3 números:")
a = int( input("a: "))
b = int( input("b: "))
c = int( input("c: "))
print("-------------------------------------------------------")
#Proceso
if a < 0 :
    r = a*b*c
else:
    r = a + b + c
print(r)