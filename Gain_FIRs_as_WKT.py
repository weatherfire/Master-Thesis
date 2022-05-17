for fc in arcpy.ListFeatureClasses():
 print(fc)

 for row in arcpy.da.SearchCursor("FIRs_FeatureToPolyg_Dissolve", ["OID@", "SHAPE@WKT"]):
  # Print feature ID
  print("FIRs_FeatureToPolyg_Dissolve", " Feature {}:".format(row[0]))
  # Print geometry as WKT
  print (row[1])

 for row in arcpy.da.SearchCursor("FIRs_FeatureToPolyg", ["OID@", "SHAPE@WKT"]):
  # Print feature ID
  print("FIRs_FeatureToPolyg", " Feature {}:".format(row[0]))
  # Print geometry as WKT
  print (row[1])


