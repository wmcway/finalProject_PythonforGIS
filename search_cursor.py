#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wmcway
#
# Created:     08/03/2017
# Copyright:   (c) wmcway 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import os

csvname = "C:\Projects\Output\StationLocations.csv"
headers = 'Bus Line Name', 'Bus Stop ID', 'X', 'Y'
createCSV(headers, csvname, 'wb')
sql = "(NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza') OR (NAME = '71 OB' AND BUS_SIGNAG = '48th Avenue')"
with arcpy.da.SearchCursor(Bus_Stops,['NAME', 'STOPID', 'SHAPE@XY'], sql) as cursor:
    for row in cursor:
        linename = row[0]
        stopid = row[1]
        locationX = row[2][0]
        locationY = row[2][1]
        locationY = row[2][1]
        data = linename, stopid, locationX, locationY

createCSV(data, csvname)

spatialReference = arcpy.SpatialReference(4326)
sql ="(NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza') OR (NAME = '71 OB' AND BUS_SIGNAG = '48th Avenue')"
dataList = []
with arcpy.da.SearchCursor(Bus_Stops,['NAME', 'STOPID', 'SHAPE@XY'], sql, SpatialReference) as cursor:
    for row in cursor:
        linename = row[0]
        stopid = row[1]
        locationX = row[2][0]
        locationY = row[2][1]
        locationY = row[2][1]
        data = linename, stopid, locationX, locationY
        if data not in dataList:
            dataList.append(data)

csvname = "C:\Projects\Output\StationLocations.csv"
headers = 'Bus Line Name', 'Bus Stop ID', 'X', 'Y'
createCSV(headers, csvname, 'wb')
for data in dataList:

sql = "OBJECTID = 1"
with arcpy.SearchCursor(BusStops, ['STOPID', 'NAME', 'OID@'], sql) as cursor:
    for row in cursor:

