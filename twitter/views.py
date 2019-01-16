from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def twitterView(request):
    return HttpResponse('BOT ACTIVE: The twitter bot is now active, tweet to @karmanishth with a substring #BUZZ (in any case)')

import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from .keys import *

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = f_read.read().strip()
    if last_seen_id is not '':
        last_seen_id = int(last_seen_id)
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.

    if last_seen_id == '':
        mentions = api.mentions_timeline(tweet_mode = 'extended')
    else:
        mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#buzz' in mention.full_text.lower():
            print('found #buzz!', flush=True)
            print('responding back...', flush=True)
            message = '@' + mention.user.screen_name + ' back to you!'
            api.update_status(message, mention.id)
            print('tweet sent')

# while True:
#     reply_to_tweets()
#     time.sleep(30)