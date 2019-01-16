# twitter-bot
A twitter bot that talks back to you when you tweet at @karmanishth with the substring #buzz. 
A twitter bot that talks back to you when you tweet at [@karmanishth](https://twitter.com/karmanishth) with the substring `#buzz`. 


# Tech Stack 
1. Python3.7, pipenv
3. Django 2.1
4. Tweepy

# How to setup the code ?
1. Assuming you have pipenv installed, (if not, run command -- `$pip install pipenv`)
2. cd inside the project directory
3. Run command -- `$pipenv install`
4. Now run the server by running command -- `$python3 manage.py runserver`
3. If you login to your local server now, you should be able to see a message saying `BOT ACTIVE`. 

PLEASE NOTE: I have not committed the twitter_keys.py file to master due to security reasons. This file goes in the /twitter/ directory as twitter_keys.py and has the following attributes that I extracted from my twitter account. \
'CONSUMER_KEY = <>\
CONSUMER_SECRET = <>\
ACCESS_KEY = <>\
ACCESS_SECRET = <>'\

If you need to replicate the environment with my keys, feel free to drop a pull request and I will be happy to connect with you over the same.

# How the bot works ?
1. Log in to your twitter account
2. Write a tweet to @karmanishth, make sure you have the keyword #BUZZ (any case) in your tweet.
3. Within 30 seconds of you tweeting, the bot talks back to you in tweet

# Sometimes...
I am not keeping the bot server active 24x7. Although I do strive to keep it always active but sometimes its just sleeping so sorry for that. It will tweet back whenever it comes back up though
