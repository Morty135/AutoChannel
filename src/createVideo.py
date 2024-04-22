from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.resize import resize
import os
from os.path import isfile, join
import random
import shutil 
from collections import defaultdict

VideoFileClip.resize = resize

# Define the target resolution
target_width = 1920
target_height = 1080

numVids = 10
vidList = []

# Populate vidList with file paths
for i in range(numVids):
    vidList.append("reddit_videos/Clip_" + str(i) + ".mp4")

# Load clips and resize them
clips = [VideoFileClip(file, target_resolution=(target_width, target_height)) for file in vidList]

# Randomize the order of clips
random.shuffle(clips)

# Concatenate the clips together
final_clip = concatenate_videoclips(clips, method="compose")

# clip resize makes it crash
#final_clip = final_clip.resize(width=1920)
#final_clip = final_clip.resize(height=1080)

# Export the final concatenated clip
final_clip.write_videofile("output.mp4", codec="libx264", audio_codec="aac", fps=24, threads=24, remove_temp=True)