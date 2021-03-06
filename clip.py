import os

#Cliping functions. Cut the boundaries outside the given shapefile. The shape file should be named "alla_lan".
def clip_operation(list_folder, source, path):
    print(path)
    if path.endswith("Layer1/"):
        clipName = "clip1_"
        mosaicName = "Mosaic1_"
    if path.endswith("Layer5/"):
        clipName = "clip5_"
        mosaicName = "Mosaic5_"

    for files in source:
        file_name = (files[8:16])
        if files.endswith(".tif") and file_name not in list_folder:
            list_folder.append(file_name)

    for name in list_folder:
        os.system("gdalwarp -co COMPRESS=DEFLATE -dstalpha -cutline alla_lan.shp -crop_to_cutline " + path + mosaicName + name + "_.tif "+ path + clipName + name+".tif")
    #In case you want to remove the mosaic files after clipping, uncomment the following line.
    #os.system("rm " + path + "/Mosaic*")

clip_operation([], os.listdir("./Layer1"), os.path.dirname(os.path.realpath(__file__))+"/Layer1/")
clip_operation([], os.listdir("./Layer5"), os.path.dirname(os.path.realpath(__file__))+"/Layer5/")
