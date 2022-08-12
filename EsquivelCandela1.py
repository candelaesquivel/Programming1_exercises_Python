'''
Ejercicio 


Una empresa de venta de articulos del hogar posee empleados con un salario básico y un adicional por hora trabajada. 
Calcular e informar para cada empleado su sueldo. Finalizar la carga de datos con -1
a) Informar el sueldo promedio.
b) Cantidad de empleados con sueldo superior al sueldo básico de la empresa. 
'''
#ingreso de el salario básico
salariobasico=int(input("ingrese el valor de salario basico:"))
#validez de el valor ingresado
while salariobasico <= 0 :
    print("ERROR")
    salariobasico=int(input("ingrese un valor VALIDO de salario basico:"))
#ingreso de el valor de el adicional por hora trabajada
adicional=int(input("ingrese el valor de el adicional x hora trabajada:"))
while adicional <= 0 :
    print("ERROR")
    adicional=int(input("ingrese un valor VALIDO de el valor del adicional x hora trabajada :"))
#ingreso de las horas trabajadas por uno de los empleados 
horastrabajadas=int(input("ingrese las horas trabajadas de un empleado (-1 para finalizar) ,(0 si tiene licencia) :"))
#valido el valor de horas trabajadas
while horastrabajadas < 0 and horastrabajadas != -1:
    print("ERROR")
    horastrabajadas=int(input("ingrese un valor VALIDO de las horas  trabajadas  de un empleado :"))
#variables
cant=0
suma=0
cantsueldomayor=0
#finalizo con -1 el ciclo 
while horastrabajadas != -1 :
    sueldo= salariobasico + horastrabajadas*adicional
#muestro el sueldo de el empleado 
    print("el sueldo de este empleado es :",sueldo)
    horastrabajadas=int(input("ingrese las horas trabajadas de un empleado (-1 para finalizar):"))
#valido el valor de horas trabajadas
    while horastrabajadas < 0 and horastrabajadas != -1:
        print("ERROR")
        horastrabajadas=int(input("ingrese  un valor VALIDO las horas trabajadas de un empleado :"))   
#calculo cantidad de empleados con sueldo superior al sueldo básico de la empresa
    if sueldo > salariobasico:
       cantsueldomayor=cantsueldomayor+1
#valores que me sirven para calcular el promedio
    suma=suma+sueldo
    cant=cant+1
if cant > 0 :
#evito la division por 0
    promedio= suma / cant
#a) Informar el sueldo promedio.
    print("el sueldo promedio es:",promedio)
#b) Informar cantidad de empleados con sueldo superior al sueldo básico de la empresa. 
    print("Cantidad de empleados con sueldo superior al sueldo básico de la empresa", cantsueldomayor)
else:
#si no ingreso empleados
    print("no se ingresaron sueldos de empleados")