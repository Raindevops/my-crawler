from youtubesearchpython import PlaylistsSearch
import csv
import subprocess
import os

# Get data from CSV
# Search the playlist on yt
# download to path

with open('musics/metal/crawl-top-200.csv', 'r') as file:
    reader = csv.reader(file)
    playlist = []
    for row in reader:
            playlist.append(row[0] + ' ' + row[1]) 


def get_playlist_url():

    search = []
    for item in playlist:
        search.append(PlaylistsSearch( item, limit=1).result())

    links = []

    for result in search:
        for item in result['result']:
            links.append(item['link'])

    return links


def download_playlists():
    urls = get_playlist_url()
    index = 0
    for url in urls:
        if not os.path.exists('musics/metal/' + playlist[index]):
            os.makedirs('musics/metal/' + playlist[index])
        subprocess.run([
                'youtube-dl',
                url ,
                '-x', 
                '--audio-format', 
                'mp3', 
                '--audio-quality', 
                '0', 
                '--yes-playlist',
                '-o',
                "musics/metal/" + playlist[index] +'/%(title)s-%(id)s.%(ext)s'
            ])
        index+=1

download_playlists()