'''
Esquivel Candela , Legajo: 1134110
EJERCICIO 1- Segundo Parcial

'''
#importamos 
from pila import *
from cola import *

#funciones

def cargarPila(pila):
    '''Recibimos una pila y la cargamos de elementos que se ingresan por teclado verificando
       que no esten repetidos

    '''
    
    pilaAux=inicializar_pila()
    pilaAux2=inicializar_pila()
        
    pasadas=0
    
    while True:
        cont=0
        
        elemento=input("ingrese un elemento a la pila (-1 para finalizar): ")
        
        #aumento por cada vez que comparo
        pasadas+=1
        
        
        if elemento=='-1':break
        
        #no agregamos a la pila si ingresa espacio 
        if elemento !='' :
            #segun la pasada usamos la pilaAux o la pilaAux2, que tendra los elementos a comparar
            if pasadas%2==0:
                
                apilar(pilaAux,elemento)
                
                while not pila_vacia( pilaAux) :
                    if elemento == tope(pilaAux):
                        #suma 1 a contador cada vez que sea repetido el elemento en una pilaAux
                        cont+=1
                    
                    apilar(pilaAux2,tope(pilaAux))
                    desapilar(pilaAux)
            else:              
                apilar(pilaAux2,elemento)
                
                while not pila_vacia( pilaAux2) :
                    if elemento == tope(pilaAux2):
                        cont+=1
                    
                    apilar(pilaAux,tope(pilaAux2))
                    desapilar(pilaAux2)
                    
            #si no genera repeticion (osea menor o igual 1 contador) el elemento se agrega a la pila        
            if cont <=1:
                apilar(pila,elemento)


def inclusionPilas(pila1,pila2):
    '''Recibimos dos pilas , verificamos simulando conjuntos si la pila1 esta incluida en la pila2
       luego devolvemos a las pilas parametros sus elementos 
       retornamos True o False referido a la inclusion 

    '''
    
    pila3=inicializar_pila()
    pila4=inicializar_pila()
    
    condicion=True
    pasadas=0
    
    #si ambas estan vacias o la primera pila lo esta la condicion es True por teoria de conjuntos) y no entra a comparar 
    if not( pila_vacia(pila1) and  pila_vacia(pila2)) or not pila_vacia(pila1) :
        while not pila_vacia(pila1) :
            
            pasadas+=1
            
            cont=0
            
            if pila_vacia(pila2):
                
                while not pila_vacia(pila3):
                    pasadas+=1
                    if tope(pila1) == tope(pila3):
                        cont+=1
                    
                    apilar(pila2,tope(pila3))
                    desapilar(pila3)  
            else:              
                while not pila_vacia(pila2):
                    if tope(pila1) == tope(pila2):
                        cont+=1
                    
                    apilar(pila3,tope(pila2))
                    desapilar(pila2)  
              
            if cont==0:
                condicion=False
            
            
            apilar(pila4,tope(pila1))
            desapilar(pila1)
            
       
        pasarEleDeUnaPilaOtra(pila4,pila1)
        
        if pila_vacia(pila2):
            pasarEleDeUnaPilaOtra(pila3,pila2)

        
    return condicion

   
def pasarEleDeUnaPilaOtra(pilA,pilB):
    '''Recibimos dos pilas y pasamos los elementos de la primera a la segunda pila
    '''
    while not pila_vacia(pilA):
        apilar(pilB,tope(pilA))
        desapilar(pilA)

def mostrarPantalla(condicion,X,Y):
    '''Recibimos una condicion booleana y dos parametros de X e Y, segun condicion True o False
       mostramos por pantalla un mensaje
    '''
    #chequeamos que sea un valor booleano antes de trabajarlo
    if condicion == True or condicion ==False:
        if condicion:
            print(f"La pila {X} esta incluida en la pila {Y}")
        else:
            print(f"La pila {X} esta NO ESTA incluida en la pila {Y}")
        
        
#programa
def main():
    '''Inicializamos dos pilas , las cargamos con elementos sin repetidos (simulando conjuntos), luego
       cheuqueamos si la pila A esta incluida en la pila B y viceversa , mostrando por pantalla
       si la inclusion se da o no

    '''
   
    pilaA=inicializar_pila()
    cargarPila(pilaA)
    
    pilaB=inicializar_pila()
    cargarPila(pilaB)

    cond=inclusionPilas(pilaA,pilaB)
    mostrarPantalla(cond,'A','B')

    cond2=inclusionPilas(pilaB,pilaA)
    mostrarPantalla(cond2,'B','A')

    
if __name__=="__main__":
    main()
    