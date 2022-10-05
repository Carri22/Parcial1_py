'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
from funciones import *

def starwars_app():
    lista_personajes = cargar_json("PP_STARWARS/data.json")
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            print("1 - Listar los personajes ordenados por altura\n")
            lista_personajes= (listar_por_key(lista_personajes, "height"))
            mostrar(lista_personajes)
        elif(respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            print (busca_personaje_mas_alto_por_genero(lista_personajes,"male"))
            print (busca_personaje_mas_alto_por_genero(lista_personajes,"female"))
        elif(respuesta=="3"):
            print("3 - Ordenar los personajes por peso\n")
            lista_personajes=listar_por_key(lista_personajes, "mass")
            mostrar(lista_personajes)
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")
            respuesta = input("Ingrese el nombre del heroe que quiere buscar \n")
            validar = validar_texto(respuesta, lista_personajes)
            print(validar) 
            print("\n")
        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")
            exportar_csv(lista_personajes, "PP_STARWARS/Archivo.csv")
        elif(respuesta=="6"):
            break


starwars_app()

