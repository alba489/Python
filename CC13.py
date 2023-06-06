print("-------------------------------------------------------")
print("Complemento 13")
print("-------------------------------------------------------")
#Entradas
ce = int( input("Ingrese la cantidad de empleados: "))
i = 1
smayor = 0.0
#Proceso
print("Ingrese los sueldos: ")
while i <= ce :
    sueldo = float( input("Ingrese sueldo: "))
    if sueldo > smayor :
        smayor = sueldo
        c = i
    i = i + 1
#Salida
print ("El empleado numero ", c, "tiene el mayor sueldo que es: ", smayor)