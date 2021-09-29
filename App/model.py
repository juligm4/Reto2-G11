"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def newCatalog():
    """
    Inicializa el catálogo de obras. Retorna el catalogo inicializado.
    """
    catalog = {'Artworks': None,
               'Artists': None}

    catalog['Artworks'] = lt.newList("ARRAY_LIST")
    catalog['Artists'] = lt.newList("ARRAY_LIST", cmpfunction=compareArtists)

    return catalog

def addArtworks(catalog, Artworks):

    lt.addLast(catalog['Artworks'], Artworks)

    constituentID = Artworks['ConstituentID'].split(",")

def addArtists(catalog, Artists):
    
    lt.addLast(catalog['Artists'], Artists)

    constituentID = Artists['ConstituentID'].split(",")


# Funciones para agregar informacion al catalogo


# Funciones para creacion de datos

def newArtist(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artist = {'name': "", "Artworks": None}
    artist['name'] = name
    artist['Artworks'] = lt.newList()
    return artist

# Funciones de consulta

def addWorkArtist(catalog, codes):
    
    list = lt.newList('ARRAY_LIST')

    for i in lt.iterator(catalog['Artworks']):
        diccionario = {}
        if codes in i['ConstituentID']:
            diccionario[i['Title']] = [codes]
            lt.addLast(list, diccionario)
    return list

# Funciones utilizadas para comparar elementos dentro de una lista


def compareArtists(artist1, artist):
    if (str(artist1) in str(artist)):
        return 0
    return -1

# Funciones de ordenamiento

def compareYears(artist2, artist1):
    if int(artist2['BeginDate']) < int(artist1['BeginDate']):
        return artist2

def compareDate(date1, date2):
    if date2['DateAcquired'] < date1['DateAcquired']:
        return date1
    
def comparePalabras(palabra1, palabra2):
    if palabra2 < palabra1:
        return palabra1

# Funciones de ordenamiento
