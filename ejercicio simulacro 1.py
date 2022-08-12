'''
1)  Generar una lista de N elementos de dos dígitos creados al azar.
Mostrar la lista.
Luego Se pide ingresar un valor y eliminar todas sus ocurrencias de la lista
, no debe quedar ningún ejemplar del número a eliminar, informar cuántas veces fue eliminado.
Desarrollar una función para eliminar todas las ocurrencias de un número y retornar la cantidad
de veces que fue eliminado.
'''
import random
#funcion
def crearlista(N):
    i=0
    lista=[]
    while i < N:
        lista.append(random.randint(10,12))
        i=i+1
    return lista

#Desarrollar una función para eliminar todas las ocurrencias de un número y retornar la cantidad de veces que fue eliminado.
def eliminarNumero(lista,n):
    cont=0
    posiciones=[]
    for i in range (len(lista)):
        if lista[i] == n:
            cont=cont+1
            posiciones.append(i)
    i=len(posiciones)
    while i > 0:
        lista.pop(posiciones[i-1])
        i=i-1
        
    print(posiciones)       
    print("La nueva lista quedo asi :",lista)
    
    return cont
            

#programa
#Generar una lista de N elementos de dos dígitos creados al azar
elementos=int(input("ingrese la cantidad de elementos a crear en la lista:"))
listacreada= crearlista(elementos)
#Mostrar la lista
print("La lista creada es :", listacreada)
#ingresar un valor y eliminar todas sus ocurrencias de la lista
numero=int(input("ingrese el numero a eliminar de la lista:"))
print("El numero fue eliminado ",eliminarNumero(listacreada,numero),"veces")
