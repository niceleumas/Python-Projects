from pytube import YouTube as YT
from pytube.exceptions import PytubeError
from datetime import timedelta

'''
Made by https://github.com/niceleumas
Do anything with the programm as long as you give the credits to me!
'''

while True:

    #URL
    error = True
    while error == True:
        try:
            url = input("URL: ")
            yt = YT(url)
        except PytubeError:
            print(f"{url} is not a valid video URL or the video is private/unavailable!\nTry later again if you think this is a mistake.")
            error = True
        else:
            error = False

    #DETAILS
    input_ = input("Do you want to show the details of the video or write it to a file ? (yes/no/write)\n").lower()
    if input_ == "yes":
        print(f"\n\nTitle: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"URL: {yt.watch_url}")
        print(f"Views: {yt.views}")
        print(f"Publish date: {str(yt.publish_date)[:-9]}")
        print(f"Keywords: {', '.join(yt.keywords)}")
        print(f"Length: {str(timedelta(seconds=yt.length))}")
        print(f"Description:\n{yt.description}\n\n")
    elif input_ == "write":
        with open("details.txt","w",encoding="utf-8") as f:
            f.write(f"Title: {yt.title}\nAuthor: {yt.author}\nURL: {yt.watch_url}\nViews: {yt.views}\nPublish date: {str(yt.publish_date)[:-9]}\nKeywords: {', '.join(yt.keywords)}\nLength: {str(timedelta(seconds=yt.length))}\nDescription:\n{yt.description}")
        print("Wrote the details to details.txt.")

    #DOWNLOAD
    input_ = input("Do you want to download the video? (yes/no)\n").lower()
    if input_ == "yes":
        input_ = input("Do you want to download the highest or the lowest resolution or only the audio? (high/low/audio)\n").lower()
        video = yt.streams
        if input_ == "high":
            print(f"Getting highest resolution ({video.get_highest_resolution().resolution}px, {video.get_highest_resolution().filesize_mb}mb, {video.get_highest_resolution().fps}fps)")
            video.get_highest_resolution().download()
        if input_ == "low":
            print(f"Getting lowest resolution ({video.get_lowest_resolution().resolution}, {video.get_lowest_resolution().filesize_mb}mb, {video.get_lowest_resolution().fps}fps)")
            video.get_lowest_resolution().download()
        if input_ == "audio":
            print(f"Getting only audio ({video.get_audio_only().filesize_mb}mb)")
            video.get_audio_only().download()
    
    print("Done!")