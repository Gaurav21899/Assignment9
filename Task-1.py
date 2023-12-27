import arcpy

pro_project_path = r"D:\Programming for GIS-3\Assignment9\Assignment_9_ProProject\MyProject.aprx"

my_project = arcpy.mp.ArcGISProject(pro_project_path)

maps_list = my_project.listMaps()

for map in maps_list:
    print("Layers in Map: {} are as follows:".format(map.name))
    for layer in map.listLayers():
        print(layer.name)

