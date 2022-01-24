## Meme Videos
Scrapes memes from reddit using praw and request and then converts them into a video using moviepy.

## Requirements
- Python 3
- Pip (Python's Package Manager)

## Installation
- First, clone the repository.
```
git clone https://github.com/daspartho/meme-videos.git 
```
- Then, change your current directory into the meme-videos repository.
```
cd meme-videos
```
- Finally, install required libraries
```
pip install requests moviepy praw
```
- From here, the program is installed. Continue to the Setting Up section in order to connect the program to reddit itself.

# Setting up

You should need to do these only the first time.

1. Make sure you have a reddit account firsthand.
2. Go to https://www.reddit.com/prefs/apps/ and sign in with your reddit account.
3. Click on the 'create app' option and provide an app name and app description as you'd like.
4. Select the script option.
5. Fill in the Redirect URIs placeholder with http://localhost:8080/, and click on 'create app'.
5. Copy the **Name**, **Client ID** and **Client Secret** and paste it in their respective placeholders in the script.
   - ⚠️ **Please remember to never share your Client Secret with anyone. This could lead to your account getting stolen or irregular Reddit user behavior that could lead to account termination.**
   - **Developers will never ask for your Client Secret.**


## Usage
Run the script from a terminal using
```
python main.py 
```

## Contributing
If you want to contribute code, just write a quick pull request and the developers will take a look at it.
If you want to suggest an idea, just write an issue and the developers will check it out!
