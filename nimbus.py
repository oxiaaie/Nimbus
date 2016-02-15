#!/usr/bin/python

import praw

r = praw.Reddit(user_agent='api_test')
submissions = r.get_subreddit('netsec').get_new(limit=5)
for submission in submissions:
    print "--------------------------------------------"
    print "Title: ", submission.title
    print "Link: ", submission.permalink
    print
    print submission.selftext
