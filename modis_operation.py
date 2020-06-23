import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def modis_operation(list_folder, source):
    path = os.path.dirname(os.path.realpath(__file__))
    for files in source:
        folder_name = (files[8:16]+"_")
        if files.endswith(".hdf") and folder_name not in list_folder:
            createFolder('./' + str(folder_name) + '/')
            list_folder.append(folder_name)


    os.system("modis_mosaic.py -o /Mosaic -v ./files.txt")
    for name in list_folder:
        os.system("modis_convert.py -v -s \"( 1 )\" -o ./Layer1/Mosaic1_"+str(name)+" -e 4326 "+ path + "/"+str(name)+"/Mosaic_LST_Day_1km.vrt") #Mosaic for Layer 1
        os.system("modis_convert.py -v -s \"( 1 )\" -o ./Layer5/Mosaic5_"+str(name)+" -e 4326 "+ path + "/"+str(name)+"/Mosaic_LST_Night_1km.vrt") #Mosaic for Layer 5
        shutil.rmtree(path + "/"+str(name)+"/")
modis_operation([], os.listdir("./"))
