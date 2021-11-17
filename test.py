from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('OrelSan', limit = 1).result()['result']

for video in videosSearch:
    print(video['link'])



# from youtubesearchpython import PlaylistsSearch

# search = PlaylistsSearch('erutan raindancer', limit=12)
# playlist = search.result()
# for video in playlist['result']:
#     print(video['title'])