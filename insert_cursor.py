#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wmcway
#
# Created:     14/03/2017
# Copyright:   (c) wmcway 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import os


Bus_Stops = r'C:\Projects\PacktDB.gdb\TestBusStops'
insertCursor = arcpy.da.InsertCursor(Bus_Stops, ['SHAPE@', 'NAME', 'STOPID'])
coordinatePair = (6001672.5869999975, 2091447.0435000062)
newPoint = arpy.Point(*coordinatePair)
dataList = [newPoint, 'NewStop1', 112121]
inertCursor.insertRow(dataList)
del insertCursor

BusStops = r'C:\Projects\PacktDB.gdb\TestBusStops'
listOfLists = [[(6002672.58675, 2092447.04362), 'NewStop2', 112122], [(6003672.58675, 2093447.04362), 'NewStop3', 112123], [(6004672.58675, 2094447.04362), 'NewStop4', 112124]]
with arcpy.da.InsertCursor(Bus_Stops, ['SHAPE@', 'NAME', 'STOPID']) as iCursor:
    for dataList in listOfLists:
        newPoint = arcpy.Point(*dataList[0])
        dataList[0] = newPoint

listOfPoints =[(6002672.58675, 2092447.04362), (6003672.58675, 2093447.04362), (6004672.58675, 2094447.04362)]
line = 'New Bus Line'
lineID = 12345
busLine = r'C:\Projects\PacktDB.gdb\TestBusStops'
insertCursor = arcpy.da.InsertCursor(busLine, ['SHAPE@', 'LINE', 'LINEID'])
lineArray = arcpy.Array()
for pointsPair in listOfPoints:
    newPoint = arcpy.Point(*pointsPair)
    lineArray.add(newPoint)

newLine = arcpy.Polyline(lineArray)
insertData = newLine, line, lineID

listOfPoints =[(6002672.58675, 2092447.04362), (6003672.58675, 2093447.04362), (6004672.58675, 2094447.04362), (6004672.58674, 2094447.04362)]
polyName = 'NewPolygon'
polyID = 54321
blockPoly = r'C:\Projects\PacktDB.gdb\TestBusStops'
insertCursor = arcpy.da.InsertCursor(blockPoly, ['SHAPE@', 'BLOCK', 'BLOCKID'])
polyArray =arcpy.Array()
for pointsPair in listOfPoints:
    newPoint = arcpy.Point(*pointsPair)
    polyArray.add(newPoint)

newPoly = arcpy.Polygon(polyArray)
insertData = newPoly, polyName, polyID
insertCursor.insertRow(insertData)
