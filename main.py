from RedditBot import RedditBot
import os
import shutil
from moviepy.editor import *

def create_video(duration_per_image=10, name='video', fps=30):
    '''creates video from the images saved in the folder'''

    # creating video
    image_folder='images'
    image_files = [os.path.join(image_folder,img)
                    for img in os.listdir(image_folder)
                    if img.endswith(".jpg")]
    frames = [ImageClip(f, duration = duration_per_image) for f in image_files]
    clip = concatenate_videoclips(frames, method='compose')
    clip.write_videofile(f"{name}.mp4", fps = fps)

    shutil.rmtree(image_folder) # deletes the images folder as no longer useful

def main():
    reddit=RedditBot()
    reddit.get_images()
    create_video()

if __name__=='__main__':
    main()