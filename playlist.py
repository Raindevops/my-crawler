from youtubesearchpython import PlaylistsSearch
import csv

# Get data from CSV
# Search the playlist on yt
# download to path

with open('musics/metal/crawl-top-200.csv', 'r') as file:
    reader = csv.reader(file)
    playlist = []
    for row in reader:
            playlist.append(row[0] + ' ' + row[1]) 


def get_playlist_url():

    print(playlist)
    search = []
    for item in playlist:
        search.append(PlaylistsSearch( item, limit=1).result())

    links = []

    for result in search:
        for item in result['result']:
            links.append(item['link'])

    return links

urls = get_playlist_url()

print(urls)