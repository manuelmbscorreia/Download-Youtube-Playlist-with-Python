#IMPORTS
import os
import moviepy.editor as mp
import re

#Path
folder = "/home/manuel/Music"

#Iteneration preparation
i = 0

#Iteneration
for file in os.listdir(folder):

    #Counting number of file
    i = i + 1
    print(f"File #{i}")

    #Manipulating files
    if re.search("mp4", file):
        mp4_path = os.path.join(folder,file)
        mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        print("New MP3 File")
        os.remove(mp4_path)
        print("Removing MP4 File")