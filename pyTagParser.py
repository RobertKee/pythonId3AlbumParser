import shutil 
from mutagen.easyid3 import EasyID3
import os.path 
from os import replace

baseDirectory = "/Users/robby/Music/iTunes/iTunes Media/Audiobooks/Rex Stout/"
titleSet = set([])

for filename in os.listdir(baseDirectory):
    if filename.endswith("mp3"):
        metadata = EasyID3(baseDirectory+filename)
        title = metadata["album"][0]
        titleSet.add(title)
        
for title in titleSet:
    titleDir = baseDirectory+title+"/"
    # print('new dir', titleDir)
    if os.path.exists(titleDir) == False:
        # print('making it')
        os.mkdir(titleDir)

for filename in os.listdir(baseDirectory):
    if filename.endswith("mp3"):
        metadata = EasyID3(baseDirectory+filename)
        title = metadata["album"][0]
        shutil.move(baseDirectory+filename, baseDirectory+title+"/"+filename)