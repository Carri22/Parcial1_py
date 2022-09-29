import re
import json

def validar_numero(patron:str,respuesta:str)->int:
    '''
    Valida si la 'respuesta' que se ingreso  por parametro puede puede castear a int

    recive una patron de tipo string, patron en forma de RegEx que permitira validar
    revice un string, string a validar
    
    Retorna el int casteado apartir del string ingresado si se pudo validar la conversion de string a int o en caso contrario retorna un -1
    '''
    if respuesta:
        if re.match(patron, respuesta):
            return(respuesta)
    return -1

def validar_lista(lista: list[dict], tamaño:int())->int:
    '''
    valida si una lista tiene una determinada cantidad de indices

    recive una lista a validar su tamaño.
    recive un int el cual representa el tamaño a validar que tenga la lista

    retorna el tamaño ingresado por parametro en caso de validar correctamente que la lista cuenta con esa cantidad de indices
    o retorna el tamaño total de indices con los que cuenta la lista en caso que el tamaño ingresado por parametro supere al de la lista 

    '''
    if lista:
        lista_tamaño=lista.copy()
        tamaño = int(tamaño)
        if tamaño>0 and tamaño <= len(lista_tamaño):
            print(f'tamaño correcto: {tamaño}')
            return tamaño
        print(f'Tamaño maximo superado, hay {len(lista_tamaño)} heroes')
        return len(lista_tamaño)

def validar_texto(pattern:str,texto:str):
    '''
    valida si el texto ingresado es correcto utilizando re.search(pattern, string)

    recive un patron y un texto, ambos de tipo string

    retorna True si el patron ingresado encuentra una coincidencia con el texto
    retorna False en caso contrario 
    '''
    if type(texto)==type("") and type(pattern)==type(""):
        texto = texto.lower()
        confirmacion = re.search(pattern, texto)
        if confirmacion == None:
           return False
        else: 
            return True 