#Descripcion de Trabajo
print("-------------------------------")
print("Ejercicio 4 Puntaje Total de Partidos")
print("-------------------------------")
#Ingreso de datos
PG=int (input("Ingrese numero de partidos ganados "))
PE=int (input("Ingrese numero de partidos empatados "))
PP=int (input("Ingrese numero de partidos perdidos "))
#Proceso
PPG=PG*3
PPE=PE*1
PPP=PP*0
PF=PPG+PPE+PPP
#Solida
print ("El puntaje total es ", PF)
 