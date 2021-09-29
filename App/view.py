﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")
    
    
    

def initCatalog():

    return controller.initCatalog()

def loadData(catalog):

    controller.loadData(catalog)

catalog = None


def last3works1(catalog):
    listWorks = lt.subList(catalog['Artworks'],-2,3)
    i = 0
    resultWorks = []
    while i < 3:
        result = listWorks["elements"][i]["Title"]
        i += 1
        resultWorks.append(result)

    return resultWorks

def last3artists1(catalog):
    listArtists = lt.subList(catalog["Artists"],-2,3)
    i = 0
    resultArtists = []
    while i < 3:
        result = listArtists["elements"][i]["DisplayName"]
        i += 1
        resultArtists.append(result)
    return resultArtists



def cronoArtists(catalog):

    controller.cronoArtists(catalog)


def cronoArtwAcqui(catalog):

    controller.cronoArtwAcqui(catalog)


def artistTechnique(catalog):

    controller.artistTechnique(catalog)

def nationalQuantity(catalog):
    controller.nationalQuantity(catalog)

#def top3last(

def departmentTransport(catalog):
    
    controller.departmentTransport(catalog)


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['Artworks'])))
        print('Artistas cargados: ' + str(lt.size(catalog['Artists'])))
        print("Los últimos tres artistas son \n")
        for i in last3artists1(catalog):
            print(i,'\n')
        print("Las últimas tres obras de arte son \n")
        for i in last3works1(catalog):
            print(i, '\n')

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
