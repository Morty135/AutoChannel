from dotenv import load_dotenv
from RedDownloader import RedDownloader


import requests
import os
import praw

load_dotenv()

# Create a Reddit instance
reddit = praw.Reddit(client_id=os.getenv("client_id"),
                     client_secret=os.getenv("client_secret"),
                     user_agent=('PyLoader by u/MortyAndTech'))

# Access a subreddit
subreddit = reddit.subreddit('funny')

download_dir = 'reddit_videos'
os.makedirs(download_dir, exist_ok=True)



limit = 50
numVids = 10
video_urls = []


for submission in subreddit.top(time_filter='day', limit=limit):
        if submission.is_video:
            video_urls.append(submission.url)
            print(submission.id)


for i in range(0, numVids):
    RedDownloader.Download(video_urls[i] , output="Clip_" + str(i) , destination=download_dir + "/")
