#IMPORTS

from pytube import YouTube as Youtube
from pytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=PLJsAc2uUPNVLMgCDC3LJG4uuzr-4wqV_K")

pasta = "/home/manuel/Music"

#Print each video url
playlist.video_urls

for url in playlist:
    try:
        Youtube(url).streams.filter(only_audio=True).first().download(pasta)
    except:
        pass
