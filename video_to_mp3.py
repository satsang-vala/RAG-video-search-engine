import os
import subprocess

files = os.listdir('Video')

for file in files:
    tutorail_name = file.split('.')[0]
    # subprocess.run(["ffmpeg","-i",f"Video/{file}",f"audios/{tutorail_name}.mp3"])
    subprocess.run(["ffmpeg", "-y", "-ss", "0", "-i", f"audios/tutorial 1.mp3", "-t", "10", "-c", "copy", "sample.mp3"])