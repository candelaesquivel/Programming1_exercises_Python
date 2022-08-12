'''
Crear una lista con números positivos desde el teclado en forma ordenada de menor a mayor hasta ingresar -1.
No se debe permitir ingresar elementos desordenados, descartarlos si esto sucede.
Crear la lista mediante una función. 
Mostrar la lista por pantalla y luego solicitar el ingreso de un número nuevo por teclado e insertarlo
en la lista de forma que mantenga el ordenamiento indicado.
No se permite ordenar Toda la lista para lograrlo, realizar desplazamientos de los elementos.
'''

#funcion

#Crear una lista con números positivos desde el teclado en forma ordenada de menor a mayor hasta ingresar -1.
def crearlista():
    
    lista=[]
    
    numero=int(input("ingrese un numero positivo en forma ordenada de menor a mayor (-1 para finalizar):"))
    while numero <0 and numero != -1:
        print("ERROR")
        numero=int(input("ingrese un numero positivo (-1 para finalizar):"))
    i=0   
    while numero !=-1:
        if i==0:
            lista.append(numero)      
        numero=int(input("ingrese un numero positivo (-1 para finalizar):"))
        while numero <0 and numero != -1:
            print("ERROR")
            numero=int(input("ingrese un numero positivo (-1 para finalizar):"))
#No se debe permitir ingresar elementos desordenados, descartarlos si esto sucede.
        if lista[i] <= numero:
            lista.append(numero)
            i=i+1
        elif i!=0:
            print("Numero desordenado , no sera agregado a la lista")
        
            
    return lista
#programa
#Crear la lista mediante una función.
listacreada= crearlista()
#Mostrar la lista por pantalla 
print(listacreada)
#y luego solicitar el ingreso de un número nuevo por teclado e insertarlo en la lista de forma que mantenga
#el ordenamiento indicado.
#No se permite ordenar Toda la lista para lograrlo, realizar desplazamientos de los elementos.

valorinsertar=int(input("ingrese el numero a insertar en la lista:"))
listacreada.append(0)
i=len(listacreada)-1
while i>0 and listacreada[i-1] > valorinsertar:
    listacreada[i]=listacreada[i-1]
    i=i-1
listacreada[i]=valorinsertar
print(listacreada)
        