'''
Esquivel Candela , Legajo: 1134110
EJERCICIO 2- Segundo Parcial

'''

#IMPORTANTE ACLARACION :
#la reunion online se evalua en el rango especificado de un dia ya que mas de 24 hs no es coherente
#(desde 6:00am hasta 15:00pm) osea que dura 9 horas que es lo que se trabaja normalmente 

#funciones
class ErrorCoherencia (Exception):pass

def chequearLegajo(legajo):
    '''Recibimos un numero de legajo , verificamos que sea de 4 numeros
       retornamos si es correcto(True) o incorrecto(False)

    '''
    chequeoLeg=False
    #pasamos a str para evitar errores por el tipo de dato que nos llegue a la funcion
    legajo=str(legajo).replace(' ','')
    if legajo.isdigit():
        #consideramos legajo valido si tiene 4 numero
        if len(legajo)==4:
            chequeoLeg=True
            
    return chequeoLeg

def chequeoNombreCompleto(nombre,i=0,chequeoNom=True):
    '''Recibimos un nombre completo, el cual puede tener hasta dos apellidos y hasta 3 nombres inclusive
       chequeamos que sea un dato valido 
       retornamos si es correcto(True) o incorrecto(False)
    '''
    if i==0:
        #pasamos a str para evitar errores por el tipo de dato que nos llegue a la funcion
        nombre=str(nombre).split()
        #usamos conjuntos para verificar que las palabras del nombre completo no esten repetidas
        nombre=list(set(nombre))
    if len(nombre)== i or chequeoNom==False:
        return chequeoNom
    else:
        nombre[i]=nombre[i].strip()
        #un nombre o apellido considero que tiene que tener un minimo de 3 letras 
        if not(nombre[i].isalpha() and len(nombre[i])>=3) or len(nombre)<2 or len(nombre)>5 :
            chequeoNom=False
            
        return chequeoNombreCompleto(nombre,i+1,chequeoNom)

def obtengoAccionUsuario(accion):
    '''Recibimos una palabra verificamos que sea 'unido' o 'abandono', sino le asignamos 'invalido'
       retornamos la palabra

    '''
    #pasamos a str para evitar errores por el tipo de dato que nos llegue a la funcion
    accion=str(accion).replace(' ','')
    accion=accion.lower()
    if not (accion=='unido'or accion=='abandono'):
        accion='invalido'
        
    return accion

def chequeoTiempo(tiempo):
    '''Recibimos un tiempo , verificamos que lo sea en el formato (hh:mm) y que este en el rango
       de las 6:00 am y 15:00pm
       retornamos True o False si el tiempo esta en la franja horaria nombrada

    '''
    chequeoT=False
    #pasamos a str para evitar errores por el tipo de dato que nos llegue a la funcion
    tiempo=str(tiempo).replace(' ','')
    if tiempo.count(':')==1:
        if tiempo[:tiempo.index(':')].isalnum() and tiempo[tiempo.index(':')+1:].isalnum():
            if int(tiempo[:tiempo.index(':')])<=15 and int(tiempo[:tiempo.index(':')])>=6:
                if int(tiempo[:tiempo.index(':')])!=15 and int(tiempo[tiempo.index(':')+1:])<=59:
                    chequeoT=True
                else:
                    if int(tiempo[tiempo.index(':')+1:])==0:
                        chequeoT=True
    return chequeoT

def chequeoHorasAbandono(entradaTiempo,salidaTiempo):
    '''Recibimos dos horarios de tiempo con formato (hh:mm), el primero refiere a un ingreso y
       el segundo a una salida en un mismo dia, si las horas de salida son menores a la de entrada
       es invalido
       retornamos True si las horas son coherentes o False caso contrario

    '''
    chequeo=False
    
    #pasamos a str para evitar errores por el tipo de dato que nos llegue a la funcion
    entradaTiempo=str(entradaTiempo).replace(' ','')
    salidaTiempo=str(salidaTiempo).replace(' ','')
    
    #si NO cumple con el formato (hh:mm) lo consideramos False ya que no es valido 
    if entradaTiempo.count(':')==1 and salidaTiempo.count(':')==1:
        
        horaEntrada,minutosEntrada=entradaTiempo.split(':')
        horaSalida,minutosSalida=salidaTiempo.split(':')
        if horaEntrada==horaSalida:
            if minutosEntrada<=minutosSalida:
                chequeo=True
        else:
            if int(horaEntrada)<int(horaSalida):
                chequeo=True
                
    return chequeo

def sumaTiempo(tiempo1,tiempo2):
    '''Recibimos dos tiempos correspondiendo el primero a una entrada y el segundo a una salida en
       un mismo dia 
       retornamos la cantidad de horas y minutos, entre ambos tiempos       
    '''
    try:
        horas=0
        tiempoFinal=0
        #chequeo formato 
        if tiempo1.count(':')==1 and tiempo2.count(':')==1:
            hora1,minuto1=(str(tiempo1).replace(' ','')).split(':')
            hora2,minuto2=(str(tiempo2).replace(' ','')).split(':')

            if hora1==hora2 and int(minuto1) <= int(minuto2):
                minutosFinal=int(minuto2)-int(minuto1)
                horaFinal='0'
            
            else:
                if int(hora2)>int(hora1):
                    cantidadHorasAminutos=(int(hora2)-int(hora1))*60
                    minutosDif=cantidadHorasAminutos+(int(minuto2)-int(minuto1))
                    while minutosDif >=60:
                        horas+=1
                        minutosDif=minutosDif-60
                    minutosFinal=minutosDif
                    horaFinal=horas
                else:
                    raise ErrorCoherencia
            tiempoFinal=str(horaFinal)+':'+str(minutosFinal)
        
        return tiempoFinal
    
    except ErrorCoherencia: pass

#funcion LAMBDA devuelve true si las pasadas consecutivas dan igual (incrementa en 1 a la pasada vieja)
consecutiv = lambda pasadaActual,pasadaVieja : pasadaActual== pasadaVieja+1

#programa

def main():
    try:
        archivo=open(r"EJERCICIO2segundoparcial.txt","r",encoding="utf-8")
    except OSError as msg:
        print(msg)
    else:
        dic={}
        dicConsecutivo={}
        dicNombresCompletos={}
        pasadas=0
        
        registro=archivo.readline()
        while registro:
            registro=registro.strip()
            
            if registro.count(';')==3:
                registro=registro.split(';')
                
                if len(registro)==4 and chequearLegajo(registro[0]) and chequeoNombreCompleto(registro[1]):                   
                    accion=obtengoAccionUsuario(registro[2])
                    tiempo=str(registro[3]).replace(' ','')
                    
                    if accion=='unido' and chequeoTiempo(tiempo):
                    
                        if registro[0] in dic:
                            nombre=dicNombresCompletos[registro[0]]
                            #si el nombre NO es igual al legajo que le corresponde NO lo consideramos los legajos son unicos tal como un DNI
                            
                            if registro[1].replace(' ','')== nombre[0].replace(' ',''):
                            #si es la segunda vez consecutiva que aparece no lo consideramos
                                
                                if not consecutiv(pasadas, dicConsecutivo.get(registro[0])):
                                    dic[registro[0]]=tiempo
                                    #el uno luego de su nombre indica que realizo un 'unido'
                                    dicNombresCompletos[registro[0]]=(registro[1],1)
                                
                    
                        else:
                            
                            dic[registro[0]]=tiempo
                            dicNombresCompletos[registro[0]]=(registro[1],1)
                            dicConsecutivo[registro[0]]=int(pasadas)
                            
                    elif accion=='abandono':
                        if chequeoHorasAbandono(dic.get(registro[0]),tiempo):
                            dic[registro[0]]=sumaTiempo(dic.get(registro[0]),tiempo)
                            #el cero luego de su nombre indica que realizo un 'abandono'
                            dicNombresCompletos[registro[0]]=(registro[1],0)
                                
            pasadas+=1
            registro=archivo.readline()
        
        for legajo in dic:
            nombre,estadoAbandono=dicNombresCompletos.get(legajo)
            print(f"\n{nombre.title()} con legajo {legajo}")
            
            if estadoAbandono == 0:
                horasPermanecidas=dic.get(legajo).split(':')
                print(f"Permanecio---> {horasPermanecidas[0]} horas y {horasPermanecidas[1]} minutos en la reunion")
            else:
                #si el usuario se unio pero luego NO abandono , su hora de abandono  es el fin de la reunion (15:00pm)
                horasPermanecidas=(sumaTiempo(dic.get(legajo),'15:00')).split(':')
                print(f"Permanecio---> {horasPermanecidas[0]} horas y {horasPermanecidas[1]} minutos en la reunion")
    
    finally:
        try:
            archivo.close()
            
        except (NameError, OSError) as msg:
            print(msg)
        
if __name__=="__main__":
    main()