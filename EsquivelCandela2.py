'''
Ejercicio 2: 
Ingresar un número numeros hasta ingresar -1 e informar:
a) cantidad de valores impares ingresados
b) cuál fue la mayor cantidad de elementos pares ingresados en forma consecutiva. 
Ejemplo: se ingresan en el siguiente orden: 2 3 4 8 10 31 2 4 -1   serian 3 numeros pares consecutivos ingresados

PROFE: se que no me dio el punto b) , pero deje hasta donde llegue a analizar. Gracias.

'''
#Ingresar un número o ingresar -1 para finalizar
numero=int(input("ingrese un numero (-1 para finalizar):"))
#variables
contimpar=0
contpar=0
contpar2=0
#comienzo del ciclo, que finaliza con -1
while numero !=-1:
#detecto si ese numero es impar
    if numero %2 != 0:
# calculo cantidad de valores impares ingresados
        contimpar=contimpar+1
#reinicio contador de numeros pares
        contpar=0
#considero cuál es numero par 
    if numero % 2 == 0 :
            
#cuanto la cantidad de numeros pares consecutivos que se va a reiniciar 
        contpar=contpar+1
#cuanto la cantidad de numeros pares consecutivos que NO va a reiniciar y le resto los impares
        contpar2=(contpar2+1)- contimpar
        if contpar2 < contpar:
            contpar2=contpar
        
    numero=int(input("ingrese un numero (-1 para finalizar):"))

#considero si el primer valor del numero es -1 y doy FIN del programa
if contimpar == 0  and contpar == 0:
    print("FIN")
else:
#cuando se ingresa -1 y NO fue el primer numero dado (el -1), muestro en pantalla los resultados 
#a) cantidad de valores impares ingresados
    print("la cantidad de valores impares ingresados son :",contimpar)
#b) cuál fue la mayor cantidad de elementos pares ingresados en forma consecutiva.
    print("la mayor cantidad de elementos pares ingresados en forma consecutiva fue :",contpar2)
        