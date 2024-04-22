from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.resize import resize
import random

# Define the target resolution
target_width = 1920
target_height = 1080

# Function to resize a clip to fit the target resolution
def resize_clip(clip):
    return clip.resize(width=target_width, height=target_height)

numVids = 10
vidList = []

# Populate vidList with file paths
for i in range(numVids):
    vidList.append("reddit_videos/Clip_" + str(i) + ".mp4")

# Load clips and resize them
clips = [resize_clip(VideoFileClip(file)) for file in vidList]

# Randomize the order of clips
random.shuffle(clips)

# Concatenate the clips together
final_clip = concatenate_videoclips(clips)

# Export the final concatenated clip
final_clip.write_videofile("output.mp4", codec="libx264", fps=24)