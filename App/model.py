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

    cat = {}

    cat['Artworks'] = lt.newList('ARRAY_LIST')

    cat['Artists'] = lt.newList('ARRAY_LIST')
    
    cat["ArtistsID"] = mp.newMap(maptype = 'PROBING', loadfactor = 0.5)

    cat["Tecnica-Medio"] = mp.newMap(maptype = 'PROBING', loadfactor = 0.5)

    cat["Nacionalidad"] = mp.newMap(maptype = 'PROBING', loadfactor = 0.5)

    return cat

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):       

    #Añadir a la Lista de Artistas
    lt.addLast(catalog['Artists'], artist)

    #Añadir al dict de IDs
    mp.put(catalog["ArtistsID"], artist["Displayname"], artist["ConstituentID"])

    #Atajo para función de Nacionalidad
    if mp.contains(catalog["Nacionalidad"], artist["Nationality"]) == False:
        init_list = [artist]
        mp.put(catalog["Nacionalidad"], artist["Nationality"], init_list) 
    
    else:
        pareja_actual = mp.get(catalog["Nacionalidad"], artist["Nationality"])
        actual_list = pareja_actual[artist["Nationality"]]
        actual_list.append(artist)
        mp.put(catalog["Nacionalidad"], artist["Nationality"], actual_list)
    
        
def addArtwork(catalog, artwork):         

    #Añadir a la lista de obras
    lt.addLast(catalog['Artworks'], artwork)

    #Atajo para función de Medios
    if mp.contains(catalog["Tecnica-Medio"], artwork["Medium"]) == False:
        init_list = [artwork]
        mp.put(catalog["Tecnica-Medio"], artwork["Medium"], init_list) 
    
    else:
        pareja_actual = mp.get(catalog["Tecnica-Medio"], artwork["Medium"])
        actual_list = pareja_actual[artwork["Medium"]]
        actual_list.append(artwork)
        mp.put(catalog["Tecnica-Medio"], artwork["Medium"], actual_list) 



# Funciones para agregar informacion al catalogo


# Funciones para creacion de datos



# Funciones de consulta



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
