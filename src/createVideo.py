from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize
import os
from os.path import isfile, join
import random

VideoFileClip.resize = resize

numVids = 10

vidList = []

for i in range(0, numVids):
    vidList.append("reddit_videos/Clip_" + str(i) + ".mp4")


clips = [VideoFileClip(file) for file in vidList]

print(clips)

for clip in clips:
    clip = clip.resize(width=1920)
    clip = clip.resize(height=1080)
    duration = clip.duration
    print(duration)

