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
    
    cat["ArtistsIDs"] = mp.newMap(maptype = 'CHAINING', loadfactor = 0.5)

    cat["Tecnica-Medio"] = mp.newMap(maptype = 'CHAINING', loadfactor = 0.5)

    cat["Nacionalidad"] = mp.newMap(maptype = 'CHAINING', loadfactor = 0.5)

    cat["FechaArtista"] = mp.newMap(maptype = "CHAINING", loadfactor = 0.5)

    cat["FechaObra"] = mp.newMap(maptype = "CHAINING", loadfactor = 0.5)

    return cat

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):       

    #Añadir a la Lista de Artistas
    lt.addLast(catalog['Artists'], artist)

    #Añadir al dict de IDs
    mp.put(catalog["ArtistsIDs"], artist["Displayname"], artist["ConstituentID"])

    #Atajo para función de Nacionalidad
    var1 = artist["Nationality"]
    if mp.contains(catalog["Nacionalidad"], var1) == False:
        init_list1 = [artist]
        mp.put(catalog["Nacionalidad"], var1, init_list1) 
    
    else:
        pareja_actual1 = mp.get(catalog["Nacionalidad"], var1)
        actual_list1 = pareja_actual1[var1]
        actual_list1.append(artist)
        mp.put(catalog["Nacionalidad"], var1, actual_list1)

    #Atajo para Nacimiento
    mp.put(catalog["FechaArtista"], artist, int(artist["BeginDate"]))

    
        
def addArtwork(catalog, artwork):         

    #Añadir a la lista de obras
    lt.addLast(catalog['Artworks'], artwork)

    #Atajo para función de Medios
    var2 = artwork["Medium"]
    if mp.contains(catalog["Tecnica-Medio"], var2) == False:
        init_list2 = [artwork]
        mp.put(catalog["Tecnica-Medio"], var2, init_list2) 
    
    else:
        pareja_actual2 = mp.get(catalog["Tecnica-Medio"], var2)
        actual_list2 = pareja_actual2[var2]
        actual_list2.append(artwork)
        mp.put(catalog["Tecnica-Medio"], var2, actual_list2) 

    #Atajo para Adquisición:
    mp.put(catalog["FechaObra"], artwork, artwork["DateAcquired"])

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
