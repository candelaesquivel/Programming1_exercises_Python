''' pilas '''
def inicializar_pila():
    pila=[]
    return pila

def apilar(pila, dato):
    pila.append(dato)
    
def desapilar(pila):
    pila.pop()
    
def tope(pila):
    return pila[-1]

def pila_vacia(pila):
    return len(pila)==0