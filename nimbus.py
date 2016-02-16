#!/usr/bin/python

import praw
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--limit','-l', type=int,
                           help='number to limit posts')
args = parser.parse_args()

r = praw.Reddit(user_agent='grabbing posts from favorite subreddits by user /u/Wh04m3y3')
submissions = r.get_subreddit('netsec+pwned').get_new(limit=(args.limit))
for submission in submissions:
    print "--------------------------------------------"
    print "Title: ", submission.title
    print "Link to Reddit: ", submission.permalink
    print "External Url: ", submission.url
    print
    print submission.selftext
