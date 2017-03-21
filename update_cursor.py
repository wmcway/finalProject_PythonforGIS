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

sql = "NAME LIKE '71%'"
with arcpy.da UpdateCursor(Bus_Stops, ['NAME'], sql),) as cursor:
    for row in cursor:
        lineName = row[0]
        newName = lineName.replace('71', '75')
        row[0] = newName

sql = 'OBJECTID < 5'
with arcpy.da.UpdateCursor(Bus_Stops, [ 'OID@', 'SHAPE@'], sql) as cursor:
    for row in cursor:
        row[1] = arcpy.Point(5999783.78657, 2088532.563956)

sql = 'OBJECTID < 5'
with arcpy.da.UpdateCursor(Bus_Stops, [ 'OID@', 'SHAPE@'], sql) as cursor:
    for row in cursor:
        print row
        row[1] = u'{"x":5999783.78657, "y":2088532.563956, "spatialReference":{"wkid":102643}}'

sql = 'OBJECTID < 2'
Bus_Stops = r'C:\Projects\PacktDB.gdb\Bus_Stops'
with arcpy.da.UpdateCursor(Bus_Stops, ['OID@, 'SHAPE@XY'], sql) as cursor:
    for row in cursor:

