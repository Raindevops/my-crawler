from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('OrelSan', limit = 1).result()['result']

for video in videosSearch:
    print(video['link'])

