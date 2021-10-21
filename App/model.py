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


from DISClib.DataStructures.arraylist import addLast
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as sa
assert cf
import time
import operator

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

    cat["Autor"] = mp.newMap(maptype = "CHAINING", loadfactor = 0.5)

    cat["Dept"] = mp.newMap(maptype = "CHAINING", loadfactor = 0.5)

    return cat

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):       

    #Añadir a la Lista de Artistas
    lt.addLast(catalog['Artists'], artist)

    #Añadir al dict de IDs
    name = artist["Displayname"]   
    name_f = name.upper()
    mp.put(catalog["ArtistsIDs"], name_f, artist["ConstituentID"])

    #Atajo para función de Nacionalidad
    var = artist["Nationality"]
    var1 = var.upper()
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
    
    ended = False
    ind = 0
    while ind < len(artwork["ConstituentID"]):
        ind_au = artwork["ConstituentID"][ind]

        if ind_au == None or ind_au == "":
            ind_au = "Sin Artista"
        if artwork["Medium"] == None or artwork["Medium"] == "":
            artwork["Medium"] = "Sin medio o tecnica"

        #Atajo para función de Medios
        print(mp.contains(catalog["Tecnica-Medio"], ind_au))

        if mp.contains(catalog["Tecnica-Medio"], ind_au) == False:

            intMap = mp.newMap(maptype = "CHAINING", loadfactor = 0.5)
            intList = lt.newList(datastructure = "ARRAY_LIST")
            lt.addLast(intList, artwork)
            mp.put(intMap, artwork["Medium"], intList)
            mp.put(catalog["Tecnica-Medio"], ind_au, intMap)
        
        else:
            if mp.contains([catalog["Tecnica-Medio"][ind_au]], artwork["Medium"]) == False:
                intlist2 = lt.newList(datastructure = "ARRAY_LIST")
                lt.addLast(intlist2, artwork)
                mp.put(catalog["Tecnica-Medio"][ind_au],artwork["Medium"], intlist2)
            
            else:
                intlist3 = [catalog["Tecnica-Medio"][ind_au][artwork["Medium"]]]
                addLast(intlist3, artwork)
        
        ind += 1

    #TODO ignora esto hasta q llegues al req4 (esto es de lo que te hablo ahí)
    #Atajo para Nacionalidad
    mp.put(catalog["Origen"], artwork, ind_au)

    #Atajo para Adquisición
    mp.put(catalog["FechaObra"], artwork, artwork["DateAcquired"])

    #Atajo para Transporte
    dep = artwork["Department"]
    dep_f = dep.upper()
    if mp.contains(catalog["Dept"], dep_f) == False:
        TintList = lt.newList(datastructure = "ARRAY_LIST")
        lt.addLast(TintList, artwork)
        mp.put(catalog["Dept"], dep_f, TintList)
    
    else:
        Tintlist2 = catalog["Dept"][dep_f]
        addLast(Tintlist2, artwork)

# Funciones de consulta

def cronoArtists(catalog):
    anio_inicial = int(input("Type the initial year of the time lapse you want to consult: "))
    anio_final = int(input("Type the end year of the time lapse you want to consult: "))
    data = lt.newList()

    for artista in catalog["FechaArtista"]:
        fecha_naci = catalog["FechaArtista"][artista]
        if fecha_naci >= anio_inicial and fecha_naci <= anio_final:
            lt.addLast(data, artista)
    
    print("There are " + str(lt.size(data)) + " artists born between " + str(anio_inicial) + " and " + str(anio_final) + "\n")
    print("The first and last 3 artists in range are... " + "\n")

    #TODO Falta la tabla y corregir el formato de los artistas correctos

def cronoArtwAcqui(catalog):
    initial_input = input("Ingrese la fecha inicial en formato AAAA/MM/DD: ")
    end_input = input("Ingrese la fecha final en formato AAAA/MM/DD: ")
    
    data = lt.newList()

    for obra in catalog["FechaObra"]:
        fecha_adqui = catalog["FechaObra"][obra]
        
        if (compareDate(initial_input, fecha_adqui) == True) and (compareDate(fecha_adqui, end_input)):
            lt.addLast(data, obra)
    
    print("The MoMA acquired " + str(lt.size(data)) + " unique pieces between " + initial_input + " and " + end_input)
    #
    #TODO Falta organizarla y corregir el formato de las obras seleccionadas

def artistTechnique(catalog):
    input_artist = input("Type the complete name of the artist you want to consult: ")
    wished_artist = input_artist.upper()
    wished_id = None
    wished_map = None
    v_tec_mas_u = None
    k_tec_mas_u = None
    num_tec_mas_u = 0
    num_obras = 0
    
    wished_pair = mp.get(catalog["ArtistsIDs"], wished_artist)
    wished_id = wished_pair[wished_artist]
    
    for cID in catalog["Tecnica-Medio"]:
        if cID == wished_id:
            wished_map == catalog["Tecnica-Medio"][cID]
            break
    
    num_tecnicas = len(mp.keySet(wished_map))

    
    for part_list in mp.valueSet(wished_map):
        num_obras += lt.size(part_list)
        if lt.size(part_list) > num_tec_mas_u:
            num_tec_mas_u = lt.size(part_list)
            v_tec_mas_u = part_list
    
    for medium in wished_map:
        if wished_map[medium] == v_tec_mas_u:
            k_tec_mas_u = medium
            break
    
    #TODO Aplicar el formato a las obras correspondiente a ese artista y la mayor tecnica. 

    print(wished_artist + " with MoMA ID " + wished_id + " has " + str(num_obras) + " pieces in his/her name at museum.")
    print("There are " + str(num_tecnicas) + " different mediums/techniques in his/her work." + "\n")
    print("Her/His top 5 Medium/Technique are: ")

    #TODO Falta la tabla tipo dict que incluya los 5 medios con mas obras.

    #TODO Falta la tabla con las 3 primeras y ultimas obras de la mejor tecnica de manera ordenada (esta lista esta alojada en la variable v_tec_mas_u). 

def nationalQuantity(catalog):
    country_dict = {}
    for pais in catalog["Nacionalidad"]:
        cantAut = lt.size(catalog["Nacionalidad"][pais])
        country_dict[pais] = catalog["Nacionalidad"][pais]
              
    data = sorted(country_dict.items(), key=operator.itemgetter(1), reverse=True)
    best_country = data.items()

    
    print("The TOP 10 Countries in the MoMA are: ")

    #TODO Falta la tabla con las 10 primeras parejas de data.

    print("The TOP nationality in the museum is: " + best_country[0][0] + " with " + best_country[0][1] + " unique pieces.")
    print("The first and last 3 objects in the " + best_country[0][0] + " artwork list are: ")
    
def departmentTransport(catalog):
    input_dept = input("Type the complete name of the department you want to transport: ")
    wished_dept = input_dept.upper()
    #TODO ya cree una rama del catalogo principal que es un mapa que divide todas las obras en departamentos.
    
    pass


    

    


    





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
        return True
    
def comparePalabras(palabra1, palabra2):
    if palabra2 < palabra1:
        return palabra1

# Funciones de ordenamiento
