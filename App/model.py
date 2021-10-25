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
import math
from tabulate import tabulate
from tabulate import _table_formats

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def newCatalog():

    catalog = {}

    catalog['Artworks'] = lt.newList('ARRAY_LIST')

    catalog['Artists'] = lt.newList('ARRAY_LIST')
    
    #Listo
    catalog["ArtistsIDs"] = mp.newMap(maptype = 'PROBING', loadfactor = 0.5)

    #Listo
    catalog["Tecnica-Medio"] = mp.newMap(maptype = 'PROBING', loadfactor = 0.5)

    #Listo
    catalog["Nacionalidad"] = mp.newMap(maptype = 'PROBING', loadfactor = 0.5)

    #Listo
    catalog["FechaArtista"] = mp.newMap(maptype = "PROBING", loadfactor = 0.5)

    #Listo
    catalog["FechaObra"] = mp.newMap(maptype = "PROBING", loadfactor = 0.5)

    #Listo
    catalog["Autor"] = mp.newMap(maptype = "PROBING", loadfactor = 0.5)

    #Listo
    catalog["Dept"] = mp.newMap(maptype = "PROBING", loadfactor = 0.5)

    return catalog

# Funciones para agregar informacion al catalogo

#Listo
def addArtist(catalog, artist):       

    #Añadir a la Lista de Artistas
    lt.addLast(catalog['Artists'], artist)

    #Añadir al dict de IDs
    name = artist["DisplayName"]   
    name_f = name.upper()
    mp.put(catalog["ArtistsIDs"], artist["ConstituentID"], name_f)

    #Atajo para función de Nacionalidad
    var = artist["Nationality"]
    var1 = var.upper()
    if mp.contains(catalog["Nacionalidad"], var1) == False:
        init_list1 = lt.newList(datastructure = "ARRAY_LIST")
        lt.addLast(init_list1, artist["ConstituentID"])
        mp.put(catalog["Nacionalidad"], var1, init_list1) 
    
    else:
        destiny1 = mp.get(catalog["Nacionalidad"], var1)
        init_list2 = me.getValue(destiny1)
        lt.addLast(init_list2, artist["ConstituentID"])

    #Atajo para Nacimiento   
    if mp.contains(catalog["FechaArtista"], int(artist["BeginDate"])) == False:
        init_list3 = lt.newList(datastructure = "ARRAY_LIST")
        lt.addLast(init_list3, artist)
        mp.put(catalog["FechaArtista"], int(artist["BeginDate"]), init_list3)
    
    else:
        destiny2 = mp.get(catalog["FechaArtista"], int(artist["BeginDate"]))
        init_list4 = me.getValue(destiny2)
        lt.addLast(init_list4, artist)
    
#Listo
def addArtwork(catalog, artwork):         

    #Añadir a la lista de obras
    lt.addLast(catalog['Artworks'], artwork)
      
    #Atajo para función de Medios
    artist_list = eval(artwork["ConstituentID"])

    if artwork["ConstituentID"] == None or artwork["ConstituentID"] == "":
            ind_au = "Sin Artista"
    
    if artwork["Medium"] == None or artwork["Medium"] == "":
            artwork["Medium"] = "Sin medio o tecnica"

    for ind in artist_list:

        ind_au = str(ind) 

        #Atajo para Nacionalidad
        if mp.contains(catalog["Autor"], ind_au) == False:
            intlist4 = lt.newList(datastructure = "ARRAY_LIST")
            lt.addLast(intlist4, artwork)
            mp.put(catalog["Autor"], ind_au, intlist4)
        
        else:
            destiny3 = mp.get(catalog["Autor"], ind_au)
            intlist5 = me.getValue(destiny3)
            lt.addLast(intlist5, artwork)

            

        if mp.contains(catalog["Tecnica-Medio"], ind_au) == False:

            intMap = mp.newMap(maptype = "PROBING", loadfactor = 0.5)
            intList = lt.newList(datastructure = "ARRAY_LIST")
            lt.addLast(intList, artwork)
            mp.put(intMap, artwork["Medium"].upper(), intList)
            mp.put(catalog["Tecnica-Medio"], ind_au, intMap)
        
        else:
            destiny1 = mp.get(catalog["Tecnica-Medio"], ind_au)
            medium_dict_map = me.getValue(destiny1)
            if mp.contains(medium_dict_map, artwork["Medium"]) == False:
                intlist2 = lt.newList(datastructure = "ARRAY_LIST")
                lt.addLast(intlist2, artwork)
                mp.put(medium_dict_map, artwork["Medium"].upper(), intlist2)
            
            else:
                destiny2 = mp.get(medium_dict_map, artwork["Medium"].upper())
                intlist3 = me.getValue(destiny2)
                addLast(intlist3, artwork)

    #Atajo para Adquisición
    
    if mp.contains(catalog["FechaObra"], artwork["DateAcquired"]) == False:
        intlist6 = lt.newList(datastructure = "ARRAY_LIST")
        lt.addLast(intlist6, artwork)
        mp.put(catalog["FechaObra"], artwork["DateAcquired"], intlist6)
    
    else:
        destiny4 = mp.get(catalog["FechaObra"], artwork["DateAcquired"])
        intlist7 = me.getValue(destiny4)
        lt.addLast(intlist7, artwork)
    
    #Atajo para Transporte
    
    
    dep = artwork["Department"]
    dep_f = dep.upper()
    if mp.contains(catalog["Dept"], dep_f) == False:
        intMap1 = mp.newMap(maptype = "PROBING", loadfactor = 0.5)
        intMap2 = priceInfo(artwork)
        mp.put(intMap1, artwork["ObjectID"], intMap2)
        mp.put(catalog["Dept"], dep_f, intMap1)
    else:
        destiny5 = mp.get(catalog["Dept"], dep_f)
        intMap3 = me.getValue(destiny5)
        intMap4 = priceInfo(artwork)
        mp.put(intMap3, artwork["ObjectID"], intMap4)
    

# Funciones de consulta


def cronoArtists(catalog):
    anio_inicial = int(input("Type the initial year of the time lapse you want to consult: "))
    anio_final = int(input("Type the end year of the time lapse you want to consult: "))

    data = []
    
    fechas = mp.keySet(catalog["FechaArtista"])
    for fecha in lt.iterator(fechas):
        if  int(fecha) >= anio_inicial and int(fecha) <= anio_final:
            destiny = mp.get(catalog["FechaArtista"], fecha)
            indArtist = me.getValue(destiny)
            for artista in lt.iterator(indArtist):
                data.append(artista)
    

    orderedData = sorted(data, key=lambda artista: artista['BeginDate'])
    


    headList = list(orderedData[0].keys())
    orderedHeadList = [headList[0], headList[1], headList[5], headList[3], headList[4], headList[2], headList[7], headList[8]]

    art1 = list(orderedData[1].values())
    art2 = list(orderedData[0].values())
    art3 = list(orderedData[2].values())
    artL1 = list(orderedData[-3].values())
    artL2 = list(orderedData[-2].values())
    artL3 = list(orderedData[-1].values())

    finalDataList = [
    [art1[0], art1[1], art1[5], art1[3], art1[4], art1[2], art1[7], art1[8]], 
    [art2[0], art2[1], art2[5], art2[3], art2[4], art2[2], art2[7], art2[8]], 
    [art3[0], art3[1], art3[5], art3[3], art3[4], art3[2], art3[7], art3[8]], 
    [artL1[0], artL1[1], artL1[5], artL1[3], artL1[4], artL1[2], artL1[7], artL1[8]], 
    [artL2[0], artL2[1], artL2[5], artL2[3], artL2[4], artL2[2], artL2[7], artL2[8]], 
    [artL3[0], artL3[1], artL3[5], artL3[3], artL3[4], artL3[2], artL3[7], artL3[8]]
    ]   

    print("There are " + str(len(data)) + " artists born between " + str(anio_inicial) + " and " + str(anio_final) + "\n")
    print("The first and last 3 artists in range are... " + "\n")
    print(tabulate(finalDataList, headers = orderedHeadList, tablefmt = "pretty") + "\n")
    
def cronoArtwAcqui(catalog):
    initial_input = input("Ingrese la fecha inicial en formato AAAA-MM-DD: ")
    end_input = input("Ingrese la fecha final en formato AAAA-MM-DD: ")
    artistList = []
    purchased = 0
    
    data = []
    orderedData = sorted(data, key=lambda obra : obra['Date'])

    fechas = mp.keySet(catalog["FechaObra"])
    for fecha in lt.iterator(fechas):
        if (compareDate(initial_input, fecha) == True) and (compareDate(fecha, end_input) == True):
            destiny = mp.get(catalog["FechaObra"], fecha)
            indVar1 = me.getValue(destiny)
            for obra in lt.iterator(indVar1):
                artistNames = ""
                if "Purchased" in obra["CreditLine"]:
                    purchased += 1
                for artistID in eval(obra["ConstituentID"]):
                    destiny2 = mp.get(catalog["ArtistsIDs"], str(artistID))
                    artistNames += str(me.getValue(destiny2)) 
                    artistNames += ", "
                    if artistID not in artistList:
                        artistList.append(artistID)
                artistNamesF = artistNames[:-2]
                obra["ArtistsNames"] = artistNamesF
                data.append(obra)
    
    orderedData = sorted(data, key=lambda obra : obra['DateAcquired'])
    

    headList = list(orderedData[0].keys())
    orderedHeadList = [headList[0], headList[1], headList[-1], headList[4], headList[5], headList[3], headList[10], headList[12]]

    art1 = list(orderedData[0].values())
    art2 = list(orderedData[1].values())
    art3 = list(orderedData[2].values())
    artL1 = list(orderedData[-2].values())
    artL2 = list(orderedData[-3].values())
    artL3 = list(orderedData[-1].values())

    finalDataList = [
    [art1[0], art1[1], art1[-1], art1[4], art1[5], art1[3], art1[10], art1[12]], 
    [art2[0], art2[1], art2[-1], art2[4], art2[5], art2[3], art2[10], art2[12]], 
    [art3[0], art3[1], art3[-1], art3[4], art3[5], art3[3], art3[10], art3[12]], 
    [artL1[0], artL1[1], artL1[-1], artL1[4], artL1[5], artL1[3], artL1[10], artL1[12]], 
    [artL2[0], artL2[1], artL2[-1], artL2[4], artL2[5], artL2[3], artL2[10], artL2[12]], 
    [artL3[0], artL3[1], artL3[-1], artL3[4], artL3[5], artL3[3], artL3[10], artL3[12]]
    ]   
    print(str(purchased))
    print("The MoMA acquired " + str(len(data)) + " unique pieces between " + initial_input + " and " + end_input)
    print("With " + str(len(artistList)) + " different artists and purchased " + str(purchased) + " of them.")
    print("The first and last artworks in the range are: " + "\n")
    print(tabulate(finalDataList, headers = orderedHeadList, tablefmt = "pretty") + "\n")
    

def artistTechnique(catalog):
    input_artist = input("Type the complete name of the artist you want to consult: ")
    wished_artist = input_artist.upper()
    wished_id = None
    wished_map = None
    tec_mas_u = None
    num_obras = 0
    
    id_list = mp.keySet(catalog["ArtistsIDs"])
    for i in lt.iterator(id_list):
        pair = mp.get(catalog["ArtistsIDs"], i)
        value = me.getValue(pair)
        if value == wished_artist:
            wished_id = i
            break
    
    
    destiny1 = mp.get(catalog["Tecnica-Medio"], wished_id)
    wished_map = me.getValue(destiny1)
            
    num_tecnicas = mp.size(wished_map)
    lista_medios = mp.keySet(wished_map)

    tabla = []

    for medio in lt.iterator(lista_medios):
        linea = [medio]
        pareja_medio = mp.get(wished_map, medio)
        lista_obras = me.getValue(pareja_medio)
        num_obras_medio = lt.size(lista_obras)
        print(num_obras_medio)
        num_obras += num_obras_medio
        linea.append(num_obras_medio)
        tabla.append(linea)

    org_tabla1 = sorted(tabla, key=lambda x:x[1], reverse=False)

    tabla1 = org_tabla1[:5]
    headliners1 = ["MediumName", "Count"]
    
    tec_mas_u = tabla1[0][0]
    v_tec_mas_u = tabla1[0][1]
    
    matriz = []
    pareja_mas_u = mp.get(wished_map, tec_mas_u)
    lista_mas_u = me.getValue(pareja_mas_u)
    for obra in lt.iterator(lista_mas_u):
        linea2 = []
        linea2.append(obra["ObjectID"])
        linea2.append(obra["Title"])
        linea2.append(obra["Medium"])
        linea2.append(int(obra["Date"]))
        linea2.append(obra["Dimensions"])
        linea2.append(obra["DateAcquired"])
        linea2.append(obra["Department"])
        linea2.append(obra["Classification"])
        linea2.append(obra["URL"])
        matriz.append(linea2)
    
    
    org_tabla2 = sorted(matriz, key=lambda x:x[3])
    #tabla2 = [org_tabla2[0], org_tabla2[1], org_tabla2[2], org_tabla2[-3], org_tabla2[-2], org_tabla2[-1]]
    tabla2_Sample = [org_tabla2[0]]
    headliners2 = ["ObjectID", "Title", "Medium", "Date", "Dimensions", "DateAcquired", "Department", "Classification", "URL"]
    



    print(wished_artist + " with MoMA ID " + wished_id + " has " + str(num_obras) + " pieces in his/her name at museum.")
    print("There are " + str(num_tecnicas) + " different mediums/techniques in his/her work." + "\n")
    print("Her/His top 5 Medium/Technique are: ")

    print(tabulate(tabla1, headers=headliners1, tablefmt="pretty") + "\n")

    print("His/Her most used Medium/Technique is: " + tec_mas_u + " with " + str(v_tec_mas_u) + " pieces.")
    print("A sample of " + tec_mas_u + " from the collection are: \n")

    print(tabulate(tabla2_Sample, headers=headliners2, tablefmt="pretty") + "\n")

    
def nationalQuantity(catalog):
    countryQuantDict = {}
    countryArtworkList = []

    paises = mp.keySet(catalog["Nacionalidad"])
    for pais in lt.iterator(paises):
        destiny2 = mp.get(catalog["Nacionalidad"], pais)
        artists_list = me.getValue(destiny2)
        total_cant_obras = 0
        if pais == "":
            pais = "UNKOWN"
        for artist in lt.iterator(artists_list):           
            destiny3 = mp.get(catalog["Autor"], str(artist))
            if destiny3 == None:
                cant_actual = 0
            else:
                cant_actual = lt.size(me.getValue(destiny3))
            total_cant_obras += cant_actual
        countryQuantDict[pais] = total_cant_obras


              
    data = dict(sorted(countryQuantDict.items(), key=lambda item: item[1], reverse=True))
    
    dataKeys = list(data.keys())
    dataValues = list(data.values())

    winNatio = dataKeys[0]
    destiny4 = mp.get(catalog["Nacionalidad"], winNatio)
    artistas = me.getValue(destiny4)
    for artista in lt.iterator(artistas):
        destiny5 = mp.get(catalog["Autor"], artista)
        if destiny5 != None:           
            var1 = me.getValue(destiny5)
            for obra in lt.iterator(var1):
                artistNames = ""
                for artistID in eval(obra["ConstituentID"]):
                    destiny6 = mp.get(catalog["ArtistsIDs"], str(artistID))
                    artistNames += str(me.getValue(destiny6)) 
                    artistNames += ", "
                artistNamesF = artistNames[:-2]
                obra["ArtistsNames"] = artistNamesF
                countryArtworkList.append(obra)

    print(countryArtworkList)
    
    finalDataList1 = [
        [dataKeys[0], dataValues[0]],
        [dataKeys[1], dataValues[1]],
        [dataKeys[2], dataValues[2]],
        [dataKeys[3], dataValues[3]],
        [dataKeys[4], dataValues[4]],
        [dataKeys[5], dataValues[5]],
        [dataKeys[6], dataValues[6]],
        [dataKeys[7], dataValues[7]],
        [dataKeys[8], dataValues[8]],
        [dataKeys[9], dataValues[9]],
    ]

    headList = list(countryArtworkList[0].keys())
    orderedHeadList = [headList[0], headList[1], headList[-1], headList[4], headList[3], headList[5], headList[9], headList[8], headList[12]]

    art1 = list(countryArtworkList[0].values())
    art2 = list(countryArtworkList[1].values())
    art3 = list(countryArtworkList[2].values())
    artL1 = list(countryArtworkList[-1].values())
    artL2 = list(countryArtworkList[-2].values())
    artL3 = list(countryArtworkList[-3].values())

    finalDataList2 = [
    [art1[0], art1[1], art1[-1], art1[4], art1[3], art1[5], art1[9], art1[8], art1[12]], 
    [art2[0], art2[1], art2[-1], art2[4], art2[3], art2[5], art2[9], art2[8], art2[12]], 
    [art3[0], art3[1], art3[-1], art3[4], art3[3], art3[5], art3[9], art3[8], art3[12]], 
    [artL1[0], artL1[1], artL1[-1], artL1[4], artL1[3], artL1[5], artL1[9], artL1[8], artL1[12]], 
    [artL2[0], artL2[1], artL2[-1], artL2[4], artL2[3], artL2[5], artL2[9], artL2[8], artL2[12]], 
    [artL3[0], artL3[1], artL3[-1], artL3[4], artL3[3], artL3[5], artL3[9], artL3[8], artL3[12]]
    ]   

    print("The TOP 10 Countries in the MoMA are: ")
    print(tabulate(finalDataList1, headers = ["Nationality", "ArtWorks"], tablefmt = "pretty") + "\n")
    print("The TOP nationality in the museum is: " + str(dataKeys[0]) + " with " + str(dataValues[0]) + " unique pieces.")
    print("The first and last 3 objects in the " + str(dataKeys[0]) + " artwork list are: ")
    print(tabulate(finalDataList2, headers = orderedHeadList, tablefmt = "pretty") + "\n")
    

  
def departmentTransport(catalog):
    input_dept = input("Type the complete name of the department you want to transport: ")
    wished_dept = input_dept.upper()
    destiny1 = mp.get(catalog["Dept"], wished_dept)
    cant_obras = lt.size(me.getValue(destiny1))
    data1 = []
    data2 = []
    total_weight = 0
    total_cost = 0
    
    destiny2 = mp.get(catalog["Dept"], wished_dept)
    for obra in me.getValue(destiny2):
        if obra["Weight"] != "":
            total_weight += obra["Weight"]
        max_price = max(mp.valueSet(obra))
        total_cost += max_price
        obra["TransCost (USD)"] = max_price
        data1.append(obra)
        data2.append(obra)
        artistNames = ""
        for artistID in obra["ConstituentID"]:
            destiny3 = mp.get(catalog["ArtistsIDs"], artistID)
            artistNames += str(me.getValue(destiny3)) 
            artistNames += ", "
        artistNamesF = artistNames[:-2]
        obra["ArtistsNames"] = artistNamesF

    orderedData1 = sorted(data1, key=lambda obra : obra['TransCost'], reverse = True)
    orderedData2 = sorted(data2, key=lambda obra : obra['Date'])

    headList1 = orderedData1[0].keys()
    orderedHeadList1 = [headList1[0], headList1[1], headList1[-1], headList1[4], headList1[3], headList1[5], headList1[9], headList1[8], headList1[12]]

    headList2 = orderedData2[0].keys()
    orderedHeadList2 = [headList2[0], headList2[1], headList2[-1], headList2[4], headList2[3], headList2[5], headList2[9], headList2[8], headList2[12]]

    art11 = orderedData1[0].values()
    art21 = orderedData1[1].values()
    art31 = orderedData1[2].values()
    artL11 = orderedData1[-1].values()
    artL21= orderedData1[-2].values()
    artL31 = orderedData1[-3].values()

    art12 = orderedData2[0].values()
    art22 = orderedData2[1].values()
    art32 = orderedData2[2].values()
    artL12 = orderedData2[-1].values()
    artL22= orderedData2[-2].values()
    artL32 = orderedData2[-3].values()


    finalDataList1 = [
    [art11[0], art11[1], art11[-1], art11[4], art11[3], art11[5], art11[9], art11[8], art11[12]], 
    [art21[0], art21[1], art21[-1], art21[4], art21[3], art21[5], art21[9], art21[8], art21[12]], 
    [art31[0], art31[1], art31[-1], art31[4], art31[3], art31[5], art31[9], art31[8], art31[12]], 
    [artL11[0], artL11[1], artL11[-1], artL11[4], artL11[3], artL11[5], artL11[9], artL11[8], artL11[12]], 
    [artL21[0], artL21[1], artL21[-1], artL21[4], artL21[3], artL21[5], artL21[9], artL21[8], artL21[12]], 
    [artL31[0], artL31[1], artL31[-1], artL31[4], artL31[3], artL31[5], artL31[9], artL31[8], artL31[12]]
    ]   
    
    finalDataList2 = [
    [art12[0], art12[1], art12[-1], art12[4], art12[3], art12[5], art12[9], art12[8], art12[12]], 
    [art22[0], art22[1], art22[-1], art22[4], art22[3], art22[5], art22[9], art22[8], art22[12]], 
    [art32[0], art32[1], art32[-1], art32[4], art32[3], art32[5], art32[9], art32[8], art32[12]], 
    [artL12[0], artL12[1], artL12[-1], artL12[4], artL12[3], artL12[5], artL12[9], artL12[8], artL12[12]], 
    [artL22[0], artL22[1], artL22[-1], artL22[4], artL22[3], artL22[5], artL22[9], artL22[8], artL22[12]], 
    [artL32[0], artL32[1], artL32[-1], artL32[4], artL32[3], artL32[5], artL32[9], artL32[8], artL32[12]]
    ]   
    
    print("The MoMA is going to transport " + str(cant_obras) + " artifacts from the " + wished_dept)
    print("REMEMBER!, Not all MoMA's data is complete!!!... These are estimates.")
    print("Estimated cargo weight (kg): " + str(total_weight))
    print("Estimated cargo cost (USD): " + str(total_cost) + "\n")
    print("The TOP 5 most expensive items to transport are: ")
    print(tabulate(finalDataList1, headers = orderedHeadList1, tablefmt = "pretty") + "\n")
    print("The TOP 5 oldests items to transport are: ")
    print(tabulate(finalDataList2, headers = orderedHeadList2, tablefmt = "pretty") + "\n")

    

    

    



    #TODO ya cree una rama del catalogo principal que es un mapa que divide todas las obras en departamentos.
    
    pass

def longlivedArtist(catalog):

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
    if date1 <= date2:
        return True
    
def comparePalabras(palabra1, palabra2):
    if palabra2 < palabra1:
        return palabra1

#Funciones Auxiliares
def priceInfo (artwork):

    intMap = mp.newMap(maptype = "PROBING", loadfactor = 0.5)

    mp.put(intMap, "ObjectData", artwork)

    mp.put(intMap, "Default", 48.00)
    
    if artwork["Weight (kg)"] != "":
        Weight = float(artwork["Weight (kg)"])*72
    else: 
        Weight = 0.0
    mp.put(intMap, "Weight", Weight)
    
    if artwork["Circumference (cm)"] != "":
        AreaCirc1 = 72 * math.pi * (float(artwork["Circumference (cm)"]) / (200 * math.pi)) ** 2
    else:
        AreaCirc1 = 0.0
    mp.put(intMap, "AreaCirc1", AreaCirc1)
    
    if artwork["Diameter (cm)"] != "":
        AreaCirc2 = 72 * math.pi * (float(artwork["Diameter (cm)"]) / 200) ** 2
    else:
        AreaCirc2 = 0.0
    mp.put(intMap, "AreaCirc2", AreaCirc2)

    if (AreaCirc1 != 0) and (artwork["Depth (cm)"] != ""):
        VolumenCirc1 = AreaCirc1 * (float(artwork["Depth (cm)"]) / 100) * 72 
    else:
        VolumenCirc1 = 0.0
    mp.put(intMap, "VolumenCirc1", VolumenCirc1)

    if (AreaCirc2 != 0) and (artwork["Depth (cm)"] != ""):
        VolumenCirc2 = AreaCirc2 * (float(artwork["Depth (cm)"]) / 100) * 72 
    else:
        VolumenCirc2 = 0.0
    mp.put(intMap, "VolumenCirc2", VolumenCirc2)

    if (AreaCirc1 != 0) and (artwork["Height (cm)"] != ""):
        VolumenCirc3 = AreaCirc1 * (float(artwork["Height (cm)"])/100) * 72 
    else:
        VolumenCirc3 = 0.0
    mp.put(intMap, "VolumenCirc2", VolumenCirc3)

    if (AreaCirc2 != 0) and (artwork["Height (cm)"] != ""):
        VolumenCirc4 = AreaCirc2 * (float(artwork["Height (cm)"])/100) * 72 
    else:
        VolumenCirc4 = 0.0
    mp.put(intMap, "VolumenCirc4", VolumenCirc4)

    if (AreaCirc1 != 0) and (artwork["Length (cm)"] != ""):
        VolumenCirc5 = AreaCirc1 * (float(artwork["Length (cm)"])/100) * 72 
    else:
        VolumenCirc5 = 0.0
    mp.put(intMap, "VolumenCirc5", VolumenCirc5)

    if (AreaCirc2 != 0) and (artwork["Length (cm)"] != ""):
        VolumenCirc6 = AreaCirc2 * (float(artwork["Length (cm)"])/100) * 72 
    else:
        VolumenCirc6 = 0.0
    mp.put(intMap, "VolumenCirc6", VolumenCirc6)

    if (AreaCirc1 != 0) and (artwork["Height (cm)"] != ""):
        VolumenCirc7 = AreaCirc1 * (float(artwork["Height (cm)"])/100) * 72 
    else:
        VolumenCirc7 = 0.0
    mp.put(intMap, "VolumenCirc7", VolumenCirc7)

    if (AreaCirc2 != 0) and (artwork["Width (cm)"] != ""):
        VolumenCirc8 = AreaCirc2 * (float(artwork["Width (cm)"])/100) * 72 
    else:
        VolumenCirc8 = 0.0
    mp.put(intMap, "VolumenCirc8", VolumenCirc8)

    if (artwork["Depth (cm)"] != "") and (artwork["Height (cm)"] != ""):
        AreaRect1 = (float(artwork["Depth (cm)"]) / 100) * (float(artwork["Height (cm)"]) / 100) * 72
    else:
        AreaRect1 = 0.0
    mp.put(intMap, "AreaRect1", AreaRect1)

    if (artwork["Depth (cm)"] != "") and (artwork["Length (cm)"] != ""):
        AreaRect2 = (float(artwork["Depth (cm)"]) / 100) * (float(artwork["Length (cm)"]) / 100) * 72
    else:
        AreaRect2 = 0.0
    mp.put(intMap, "AreaRect2", AreaRect2)

    if (artwork["Depth (cm)"] != "") and (artwork["Width (cm)"] != ""):
        AreaRect3 = (float(artwork["Depth (cm)"]) / 100) * (float(artwork["Width (cm)"]) / 100) * 72
    else:
        AreaRect3 = 0.0
    mp.put(intMap, "AreaRect3", AreaRect3)

    if (artwork["Height (cm)"] != "") and (artwork["Length (cm)"] != ""):
        AreaRect4 = (float(artwork["Height (cm)"]) / 100) * (float(artwork["Length (cm)"]) / 100) * 72
    else:
        AreaRect4 = 0.0
    mp.put(intMap, "AreaRect4", AreaRect4)

    if (artwork["Height (cm)"] != "") and (artwork["Width (cm)"] != ""):
        AreaRect5 = (float(artwork["Height (cm)"]) / 100) * (float(artwork["Width (cm)"]) / 100) * 72
    else:
        AreaRect5 = 0.0
    mp.put(intMap, "AreaRect5", AreaRect5)

    if (artwork["Length (cm)"] != "") and (artwork["Width (cm)"] != ""):
        AreaRect6 = (float(artwork["Length (cm)"]) / 100) * (float(artwork["Width (cm)"]) / 100) * 72
    else:
        AreaRect6 = 0.0
    mp.put(intMap, "AreaRect6", AreaRect6)
    
    if (artwork["Depth (cm)"] != "") and (artwork["Height (cm)"] != "") and (artwork["Length (cm)"] != ""):
        VolumenRect1 = (float(artwork["Depth (cm)"]) / 100) * (float(artwork["Height (cm)"]) / 100) * (float(artwork["Length (cm)"]) / 100)
    else:
        VolumenRect1 = 0.0
    mp.put(intMap, "VolumenRect1", VolumenRect1)
    
    if (artwork["Depth (cm)"] != "") and (artwork["Length (cm)"] != "") and (artwork["Width (cm)"] != ""):
        VolumenRect2 = (float(artwork["Depth (cm)"]) / 100) * (float(artwork["Length (cm)"]) / 100) * (float(artwork["Width (cm)"]) / 100)
    else:
        VolumenRect2 = 0.0
    mp.put(intMap, "VolumenRect2", VolumenRect2)

    if (artwork["Depth (cm)"] != "") and (artwork["Width (cm)"] != "") and (artwork["Height (cm)"] != ""):
        VolumenRect3 = (float(artwork["Depth (cm)"]) / 100) * (float(artwork["Width (cm)"]) / 100) * (float(artwork["Height (cm)"]) / 100)
    else:
        VolumenRect3 = 0.0
    mp.put(intMap, "VolumenRect3", VolumenRect3)

    if (artwork["Height (cm)"] != "") and (artwork["Length (cm)"] != "") and (artwork["Width (cm)"] != ""):
        VolumenRect4 = (float(artwork["Height (cm)"]) / 100) * (float(artwork["Length (cm)"]) / 100) * (float(artwork["Width (cm)"]) / 100)
    else:
        VolumenRect4 = 0.0
    mp.put(intMap, "VolumenRect4", VolumenRect4)

    return intMap
