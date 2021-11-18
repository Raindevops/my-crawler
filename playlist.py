from youtubesearchpython import PlaylistsSearch

search = PlaylistsSearch('erutan raindancer', limit=12)
playlist = search.result()
for video in playlist['result']:
    print(video['title'])