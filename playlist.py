from youtubesearchpython import PlaylistsSearch

search = PlaylistsSearch('Megadeth	Rust In Peace ', limit=1)
playlist = search.result()
for video in playlist['result']:
    print(video['link'])