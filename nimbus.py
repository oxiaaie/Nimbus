#!/usr/bin/python

import praw

r = praw.Reddit(user_agent='api_test')
submissions = r.get_subreddit('netsec').get_new(limit=5)
for submission in submissions:
    print "--------------------------------------------"
    print "Title: ", submission.title
    print "Link to Reddit: ", submission.permalink
    print "External Url: ", submission.url
    print
    print submission.selftext
