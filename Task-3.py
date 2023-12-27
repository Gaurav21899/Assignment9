import arcpy

pro_project_path = r"D:\Programming for GIS-3\Assignment9\Assignment_9_ProProject\MyProject.aprx"

my_project = arcpy.mp.ArcGISProject(pro_project_path)

layout_list = my_project.listLayouts()
for layout in layout_list:
    print(layout.name)

    layout.exportToPNG(r"D:\Programming for GIS-3\Assignment9\Output")

print("Layout Exported")
print("Process Completed")



