import wx
import pathlib

basepath = pathlib.Path("P:/")

def makePhotoFolder(folderName, namedSubfolders=True):
    uneditedFolder = basepath / folderName / "unbearbeitet"
    uneditedFolder.mkdir(parents=True)
    if namedSubfolders:
        SteffiFolder = uneditedFolder / "Steffi"
        SteffiFolder.mkdir(parents=True)
        ThomasFolder = uneditedFolder / "Thomas"
        ThomasFolder.mkdir(parents=True)

# makePhotoFolder("zzzTest", namedSubfolders=True)