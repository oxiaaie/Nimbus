#!/usr/bin/python

import praw

r = praw.Reddit(user_agent='grabbing posts from favorite subreddits by user /u/Wh04m3y3')
submissions = r.get_subreddit('netsec+pwned').get_new(limit=25)
for submission in submissions:
    print "--------------------------------------------"
    print "Title: ", submission.title
    print "Link to Reddit: ", submission.permalink
    print "External Url: ", submission.url
    print
    print submission.selftext
