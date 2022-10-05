import re
import json

def cargar_json(path:str)->list:
    '''
    carga un archivo de tipo json para utilizarlo
    recibe la ruta donde se encuentra el archivo
    retorna una lista con los valores del archivo json
    '''
    with open(path, "r") as file:
        listajson = json.load(file)
    return listajson["results"]    

def mostrar (lista:list):
    '''
    Imprime por consola cada indice una lista de forma en que se vea prolija
    recibe una lista
    no retorna
    '''
    if len(lista)>0:
        lista_mostrar=lista.copy()
        for elemento in lista_mostrar:
            mensaje = (f'Nombre: {elemento["name"]} | Height: {elemento["height"]} | Mass: {elemento["mass"]} | Gender: {elemento["gender"]} \n') 
            print(mensaje)  

def buscar_minimo(lista:list,key:str)->int:
    '''
    Busca el indice del valor mas bajo de una lista, dependiendo la key ingresada
    recibe una lista y un key 
    retorna un int con el valor del indice del valor minimo
    '''
    if len(lista)>0:
        lista_min=lista.copy()
        i_min=0
        i=0
        for elemento in lista_min:
            if int(elemento[key])<int(lista_min[i_min][key]):
                i_min=i
            i+=1
        return i_min


def buscar_maximo(lista:list,key:str)->int:
    '''
    Busca el indice del valor mas alto de una lista, dependiendo la key ingresada
    recibe una lista y un key 
    retorna un int con el valor del indice del valor minimo
    '''
    if len(lista)>0:
        lista_min=lista.copy()
        i_max=0
        i=0
        for elemento in lista_min:
            if int(elemento[key])>int(lista_min[i_max][key]):
                i_max=i
            i+=1
        return i_max        

def busca_personaje_mas_alto_por_genero(lista:list,genero:str):
    '''
    Busca el personaje mas alto por genero
    recibe una lista y un str con el genero "male" o "female"
    retorna un mensaje diciendo quien es el personaje mas alto dependiendo el genero ingresado por parametro
    '''
    if len(lista)>0:
        lista_altura_genero=lista.copy()
        lista_genero=[]
        for elemento in lista_altura_genero:
            if elemento["gender"]==genero:
                lista_genero.append(elemento)
        indice=buscar_maximo(lista_genero, "height")
        mensaje = (f'El personaje mas alto del genero {genero} es: {lista_genero[indice]["name"]} \n')
        return mensaje
        

def listar_por_key(lista:list,key:str)->list:
    '''
    Ordena de menor a mayor una lista a partir del valor que represente la key ingresada
    recibe una lista a ordenar y una key
    retorna una lista ordenada
    '''
    if len(lista)>0:
        lista_a_ordenar = lista.copy()
        lista_ordenada = []
        while (len(lista_a_ordenar)):
            index_minimo = buscar_minimo(lista_a_ordenar, key)
            elemento = lista_a_ordenar.pop(index_minimo)
            lista_ordenada.append(elemento)
        return lista_ordenada 

def exportar_csv(lista:list, path:str):
    '''
    Exporta un archivo csv a partir de una lista 
    recibe una lista 
    no retorna
    '''
    with open(path, "w") as file:
        for elemento in lista:
            file.write(f'{elemento}\n')

def validar_texto(nombre:str, lista:list):
    '''
   Valida si un nombre(string) se encuentra en una lista
   recibe un string y una lista 
   Si valida que el nombre se encuentra en la lista retorna el elemento de la lista que coincida , en caso de validar 
    '''
    if len(lista)>0:
        lista_validar = lista.copy()
        lista_a_validar = []
        validacion = False
        for elemento in lista_validar:
            texto = elemento["name"].lower()
            nombre=nombre.lower()
            confirmacion = re.search(nombre, texto)
            if confirmacion == None:
                pass
            else: 
                validacion = True
                lista = elemento
        if validacion ==True:
            print("\n")
            return lista
        else:
            mensaje = "El heroe ingresado no se encuentra en la lista" 
            print("\n")
            return mensaje   