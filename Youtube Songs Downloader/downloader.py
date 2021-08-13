import urllib.request
import re
from pytube import YouTube
import os

def download_song(search_keyword,limit):
    os.mkdir('downloads')
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for elem in video_ids:
        limit -=1
        link = "https://www.youtube.com/watch?v=" + elem
        try : 
            yt = YouTube(link)
        except:
            print("Network Issue")

        try: 
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download('./downloads/')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            
        except:
            print("error")

        if limit == 0 : 
            break
        

    