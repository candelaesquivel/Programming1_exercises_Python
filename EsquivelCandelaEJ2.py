#parcial2ej2
'''
Ejercicio 2: (50%)
Desarrollar un programa y las funciones que considere para generar una lista con números enteros al azar a y b. 
Finalizar la carga de la misma cuando se obtenga el valor cero, el cero no deberá cargarse en la lista y no debe quedar vacia la lista.
intercambiar los elementos de posiciones consecutivas. Informar cuantos intercambios se realizaron.'''

import random
#funciones
#validar entero
def validarEntero (numero):
    while numero < 0:
        print("ERROR , no es un numero entero")
        numero=int(input("ingrese el numero nuevamente"))
    return numero
#creo lista final         
def crearFuncion(comienzo,final):
    lista=[]
    numero=random.randint(comienzo,final)
#chequeo tener aunquesea 1 elemento en la lista y que no sea el cero 
    while numero == 0:
        numero=random.randint(comienzo,final)
#ya chequeado que no sea el 0 , lo agrego como primer elemento de la lista
    lista.append(numero)
#arranco con los demas y si el numero generado es el cero ,termina la carga de numeros en la lista y NO lo agrego como elemento
    while numero !=0:
        numero=random.randint(comienzo,final)
        if numero !=0:
            lista.append(random.randint(comienzo,final))
 
#si la lista tiene 2 elementos o mas , realizo intercambio de consecutivos . Ya que si solo tiene 1 elemento , no tiene sentido 
    if len(lista) >= 2:
        intercambioConsecutivos(lista)
    else:
        print("La cantidad de intercambios sera nula ya que solo tiene un elemento la lista")
    
   
    return lista
       
       
def intercambioConsecutivos(listaconsecutivos):
#intercambio consecutivos pero voy de 2 en 2 recorriendo sino me contempla un elemento que ya fue permutado
    cont=0
    for i in range (0,len(listaconsecutivos)-1,2):
#guardo listaconsecutivo[i] en una variable auxiliar para realizar el intercambio de consecutivos
        aux=listaconsecutivos[i]
        listaconsecutivos[i]=listaconsecutivos[i+1]
        listaconsecutivos[i+1]=aux
        cont=cont+1
#muestro por pantalla la cantidad de intercambios realizados        
    
    print("AVISO : La cantidad de intercambios realizados en la lista fueron:",cont)
        
        


#programaPrincipal
#el valor de "a" es cero ya que sino no puedo determinar mediante el rango que el cero sea considerado para finalizar el ciclo (EVITO CICLO INFINITO)
#EJEMPLO= si elije el numero a=5 , es imposible que se elija el numero 0 en algun momento al azar !
desde=int(input("ingrese el comienzo de el rango de la lista de numeros enteros (no podra ser mayor a 0)"))
while desde !=0:
    print("invalido")
    desde=int(input("ingrese el comienzo de el rango de la lista (no podra ser mayor a 0)"))
#pido el tope de rango y valido que sea entero con una funcion
hasta=int(input("ingrese el tope de rango de la lista a crear (numero entero)"))
hasta=validarEntero(hasta)
#muestro por pantalla la lista final con los intercambios de los numeros consecutivos , use una funcion para realizar la lista final 
print("La lista  final creada es :",crearFuncion(desde,hasta))