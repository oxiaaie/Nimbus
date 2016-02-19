#!/usr/bin/python

import praw
import argparse

parser = argparse.ArgumentParser(description="Adds a set of arguments from user")                                                                                                            
parser.add_argument("-l",                                                                                                                                                                     
                    "--limit",                                                                                                                                                               
                    dest='limit_posts',                                                                                                                                                      
                    type=int,                                                                                                                                                                
                    default=1,                                                                                                                                                               
                    help="Define number to limit posts")
# parser.add_argument("-s",                                                                                                                                                                     
#                     "--sub-reddit",
#                     dest='sub_reddit',
#                     type=string,
#                     default=netsec,
#                     help='Define the subreddit you want to pull the posts from')
args = parser.parse_args() 

# SUB_REDDIT = 'netsec'
# LIMIT_POSTS = 2

r = praw.Reddit(user_agent="grabbing posts from favorite subreddits by user /u/Wh04m3y3")
submissions = r.get_subreddit("netsec+pwned").get_new(limit=args.limit_posts)
for submission in submissions:
    print "--------------------------------------------"
    print "Title: ", submission.title
    print "Link to Reddit: ", submission.permalink
    print "External Url: ", submission.url
    print
    print submission.selftext