import praw
import requests
import os
import shutil
from moviepy.editor import *

def setup_reddit(id, secret, user):
    '''creating a reddit instance for scraping'''
    reddit = praw.Reddit(
            client_id=id,
            client_secret=secret,
            user_agent=user,
            )
    return reddit # returns reddit instance

def get_images(reddit_object, sub_name='memes', limit=25):
    '''scrapes reddit for memes and saves them on a folder'''

    os.makedirs('images') # creates dir that will contain the images
    sub = reddit_object.subreddit(sub_name) # creates a subreddit instance

    n=1 # n is used for naming images
    for post in sub.hot(limit=limit):
        url=post.url
        if url.endswith('.jpg'):
            img_data = requests.get(url).content
            with open(f'images\img{n}.jpg', 'wb') as handler:
                handler.write(img_data) # saving images
                n+=1

def create_video(duration_per_image=10, name='video', fps=24):
    '''creates video from the images saved in the folder'''

    # creating video
    image_folder='images'
    image_files = [os.path.join(image_folder,img)
                    for img in os.listdir(image_folder)
                    if img.endswith(".jpg")]
    frames = [ImageClip(f, duration = duration_per_image) for f in image_files]
    clip = concatenate_videoclips(frames, method = "compose")
    clip.write_videofile(f"{name}.mp4", fps = fps)

    shutil.rmtree(image_folder) # deletes the images folder as no longer useful
    os.startfile(f'{name}.mp4') # starts the video

def main():
    client_id="" # put client id here
    client_secret="" # put client secret here
    user_agent="" # put user agent here
    reddit=setup_reddit(client_id, client_secret, user_agent)
    get_images(reddit)
    create_video()

if __name__=='__main__':
    main()