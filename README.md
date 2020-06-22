# MODIS_analysis
In this repository I explain how to download MODIS data from a text file, make a reprojection and mosaic them. This can be used either in Linux or Mac. I am happy to help if there is any issue or misunderstanding in the explanation. Open a ticket issue if you need any help. 

# Prerequisites and Installation

`MODIS_Analysis` requires the following packages for installation:

1.`python3 or higher` (`$ sudo apt-get install python3.6`)

2. `GDAL` Python package

3. `pyModis` (`$ pip install pyModis`)

4. `wget` (Linux: `$ apt install wget`) (Mac: `$ brew install wget`)

# Friendly tip

My advice for successfully installing GDAL and pymodis at the same time is doing the following:
Download miniconda from https://docs.conda.io/en/latest/miniconda.html
Install miniconda with: `$ bash Miniconda3-latest-Linux-x86_64.sh`.
Create conda environment installing GDAL directly: `$ conda create -n MODIS_analysis gdal python=2.7`.
Activate the environment you just created: `$ source activate MODIS_analysis`.
Now you can install with pip any library (`$ pip install pyModis`), and they will install in the same python environment as the conda package.

Back to work, let's continue!! 

# Run example

### Let's assume everything is installed correctly and working:
If you have access to the cluster "Lancelot" (at the Luleå University of Technology), you can literally follow this example as I have already done all the previous installations.

1. Go to the folder you would like to do the run: e.g. `$ cd /data/no_backup/roberto/shaktiman_project/`
Here, create a folder with any name with the following command: `$ mkdir foldername` (Change “foldername” with the name you want)
Now go into the folder with: `$ cd foldername` (Change “foldername” with the name you chose before)

2. Make sure you clone the repository:

```
$ git clone https://github.com/RobertoMantas/MODIS_analysis.git
```

3. In the new created folder, make sure that there is a file called “links.txt” with all the links to download. For this use the following command: `$ nano links.txt` And paste the links in the new text file. Then press ctrl + x followed by “y” answering yes to save the file.
4. Run the following command to download all the wanted files listed in the “links.txt” file. If the file has a different name as e.g.”7361544994-download.txt”, change the name at the end. (Change "username" and "password" for you NASA MODIS credentials.)
```
$ wget --user "username" --password "password" -i links.txt
``` 
5. Now, in the current folder you should have all the files. The next step is to have a text file called “files.txt” in which it lists all the downloaded files to study. We can achieve this with the following command: `$ ls MOD11A1* > files.txt` Being “MOD11A1” the matching text at the beginning of all the files in which we are interested. Make sure that the rest of the files don’t start with this name. 
6. Activate the python environment where we are going to work with the following command: `$ source activate mygdalenv2` (You may have done this alredy in a previous step if you have followed the installation)
To make sure that the command worked properly, now you should see (mygdalenv2) at the beginning. eg. “(mygdalenv2) username@lancelot:/data/no_backup/roberto/shaktiman_project” 
7. We are going to create two folders in which we will have the different layers we want to extract. With the commands:
`$ mkdir Layer1 Layer5`
8. Finally, the last step would be to run the main script:
```
$ python modis_operation.py
```
In the folder Layer1 and Layer5, you will find all the files mosaic with the termination “.tif” compatible to open with any standard visualiser (QGIS, preview, ArcGIS…) 

I hope these scripts are useful for the data analysis of the MODIS data. 
