print("-------------------------------------------------------")
print("Ejercicio6")
print("-------------------------------------------------------")
#Constante
A1=1
A2=0
AN=A1+(2*A2)
CONS=0
#Proceso
while AN<300:
    A2=A1
    A1=AN
    AN=A1+(2*A2)
    CONS=CONS+1
#Salida
print("El rango es:", CONS, "y el resultado es:", AN)