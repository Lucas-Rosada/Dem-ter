import os
import yt_dlp

diretorio = 'videos/'

def download_mp3(video_url):
    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': '.mp3',
        'outtmpl': f'{diretorio}%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_url])

video_url = input("Insira a URL do vídeo do YouTube: ")
download_mp3(video_url)