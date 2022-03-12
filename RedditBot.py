import praw
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class RedditBot():

    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv('ID'),
            client_secret=os.getenv('SECRET'),
            user_agent=os.getenv('AGENT'),
        )

    def get_images(self, sub_name='memes', limit=10):
        '''scrapes reddit for memes and saves them on a folder'''

        os.makedirs('images') # creates dir that will contain the images
        
        sub = self.reddit.subreddit(sub_name) # creates a subreddit instance

        n=1 # n is used for naming images
        for post in sub.hot(limit=limit):
            url=post.url
            if url.endswith('.jpg'):
                img_data = requests.get(url).content
                with open(f'images/img{n}.jpg', 'wb') as handler:
                    handler.write(img_data) # saving images
                    n+=1  
