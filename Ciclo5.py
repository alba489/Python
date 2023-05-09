print("-------------------------------------------------------")
print("Ejercicio5")
print("-------------------------------------------------------")
#Constante
x= int(input("Ingrese un el valor de X: "))
e=1
num=1
den=1
i=1
#Proceso
num=x**i
den=den*i
i=i+1
e=e+num/den
#Ciclo
while not (num/den < 0.000001):
    num = x**i
    den = den*i
    i = i + 1
    e=e+num/den
print("e elevado al", x, "es: ", e)