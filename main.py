import praw
import requests
import os
import shutil
from moviepy.editor import *

reddit = praw.Reddit(
    client_id="", # put client id here
    client_secret="", # put client secret here
    user_agent="", # put user agent here
    )

sub = reddit.subreddit("memes")
image_folder= 'images'
n=1
for post in sub.hot(limit=10):
    url=post.url
    if url.endswith('.jpg'):
        img_data = requests.get(url).content
        with open(f'{image_folder}\img{n}.jpg', 'wb') as handler:
            handler.write(img_data)
            n+=1

image_files = [os.path.join(image_folder,img)
               for img in os.listdir(image_folder)
               if img.endswith(".jpg")]
frames = [ImageClip(f, duration = 10) for f in image_files]
clip = concatenate_videoclips(frames, method = "compose")
clip.write_videofile("video.mp4", fps = 24)

shutil.rmtree(image_folder)
os.makedirs(image_folder)
