#parcial2ej1
'''
Ejercicio 1: (50%)


Una pequeña empresa de fabricación de tortas tiene que reemplazar uno de los hornos. 
Realizó una licitación y necesita un programa que le permita tomar las decisiones correctas para decidir cuál es la mejor opción.
Sólo le interesan aquellos presupuestos menores al promedio que no superen los 10 días de entrega. Indicar cuantos se rechazaron.
Diseñe el programa que necesita la empresa para poder
obtener un listado de los proveedores ordenados de menor a mayor segun la cantidad de dias de entrega. 
Desarrolle creando y utilizando funciones.'''


#funciones

#valido que no me ingrese valores de dias y presupeustos menores o iguales a cero ya que no es coherente sino
def validarPositivo(numero):
    while numero <=0 :
        print("ERROR")
        numero=int(input("ingrese un numero positivo sino es invalido :"))
        
    return numero

#valido que no me ingrese un codigo de proveedor igual o menor que cero y permito -1 ya que indica final del ciclo
#chequeo que no pongan mismo codigo para proveedor ya que no pueden tener el mismo "nombre"
def validarPositivoFinciclo(numero,lista):
    while (numero <=0 and numero!= -1 ) or existe(numero,lista) :
        print("ERROR")
        numero=int(input("ingrese un numero positivo o ese codigo ingresado ya existe  :"))
        
    return numero
        
def seleccionProveedores(listaprov,listapresu,listadias,prom):
#creo listas con los datos de los proveedores que me interesan
    listaprovedorcorrectos=[]
    listapresupuestocorrectos=[]
    listadiascorrectos=[]
    rechazo=0
    for i in range (len(listaprov)):
# solo me quedo con los proovedores que tengan un presupuesto menor al promedio (NO IGUAL O MAYOR) y que la entrega de dias sea igual o menor a 10
        if listapresu[i] < prom and listadias[i] <= 10:
            listaprovedorcorrectos.append(listaprov[i])
            listapresupuestocorrectos.append(listapresu[i])
            listadiascorrectos.append(listadias[i])
        else:
#cuento la cantidad que rechaze
            rechazo=rechazo+1

#le digo al usuario la cantidad de rechazos             
    print("La cantidad de proveedores rechazados fue :",rechazo)
    
#ordeno de menor a mayor segun los dias de entrega con una funcion
    
    metodoSeleccionPorDias(listadiascorrectos,listapresupuestocorrectos,listaprovedorcorrectos)
    for i in range (len(listaprovedorcorrectos)):
        print("La lista de los provedores es", listaprovedorcorrectos[i]," tardan estos dias", listadiascorrectos[i], " tiene un presupeusto de :",listapresupuestocorrectos[i])
            
def metodoSeleccionPorDias(lista,lista2,lista3):
#ordenamos una lista y arrastramos dos valores con ella
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
                aux = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux
                
                aux = lista3[i]
                lista3[i] = lista3[j]
                lista3[j] = aux
                
def existe(num,lista): #BUSQUEDA SECUENCIAL de codigo de proovedores con TRUE /FALSE
    encontrado=False
    i=0
    while i < len(lista) and encontrado == False :
        if lista[i] == num:
            encontrado=True
        i = i + 1
    
    return encontrado               

#programaPrincipal

#Realizó una licitación ,creo las listas de proveedores con los presupuestos y dias de entrega de cada uno, valido valores coherentes con funciones
proveedor=int(input("ingrese codigo del proveedor (FINALIZA CON -1)"))
listaproveedor=[]
#tiene una funcion de validar distinta ya que le permito ingresar -1
proveedor=validarPositivoFinciclo(proveedor,listaproveedor)



#si no finaliza continuo
if proveedor != -1:
    presupuesto=int(input("ingrese el presupuesto del horno  :"))
    presupuesto=validarPositivo(presupuesto)
    cantidaddias=int(input("ingrese la cantidad de dias de entrega:"))
    cantidaddias=validarPositivo(cantidaddias)
    listapresupuesto=[]
    listadiasentrega=[]
    
#la suma de presupuestos arranca con este valor de presupuesto (el primero)
    presupeustosuma=presupuesto
#finalizo con proveedor = -1
while proveedor != -1:
#agrego los valores ingresados a las listas
    listaproveedor.append(proveedor)
    listapresupuesto.append(presupuesto)
    listadiasentrega.append(cantidaddias)
#vuelvo a pedir a otro proveedor hasta que el usuario quiera terminar y ponga -1
    proveedor=int(input("ingrese codigo del proveedor (FINALIZA CON -1)"))
    proveedor=validarPositivoFinciclo(proveedor,listaproveedor)

    if proveedor != -1:
        presupuesto=int(input("ingrese el presupuesto del horno  :"))
        presupuesto=validarPositivo(presupuesto)
#sumo presupuestos para calcular promedio al final y lo pongo luego del IF por que si indica -1 no quiero sumar eso 
        presupeustosuma=presupeustosuma+presupuesto
        cantidaddias=int(input("ingrese la cantidad de dias de entrega:"))
        cantidaddias=validarPositivo(cantidaddias)
    
#calculopromedio y cuido la division por cero y sigo con el programa si el primer proveedor no fue -1
if len(listaproveedor) != 0:
    promedio=presupeustosuma /len(listaproveedor)
#utilizo funcion para seleccionar los proveedores que me interesan nada mas (filtro)
    seleccionProveedores(listaproveedor,listapresupuesto,listadiasentrega,promedio)
else:
#aviso al usuario que no se ingreso ningun valor
    print("no se ingresaron valores")
        
