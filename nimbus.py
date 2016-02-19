#!/usr/bin/python

import praw
import argparse


def arguments():
    parser = argparse.ArgumentParser(description="Adds a set of arguments from user")
    parser.add_argument("-l",
                        "--limit",
                        dest='limit_posts',
                        type=int,
                        default=1,
                        help="Define number to limit posts")
    parser.add_argument("-s",
                        "--sub-reddit",
                        dest='sub_reddit',
                        type=str,
                        default="netsec+pwned",
                        help='Define the subreddit you want to pull the posts from')
    arg_x = parser.parse_args()
    return arg_x

args = arguments()


def bot():

    r = praw.Reddit(user_agent="grabbing posts from favorite subreddits by user /u/Wh04m3y3")
    submissions = r.get_subreddit(args.sub_reddit).get_new(limit=args.limit_posts)
    for submission in submissions:
        print "--------------------------------------------"
        print "Title: ", submission.title
        print "Link to Reddit: ", submission.permalink
        print "External Url: ", submission.url
        print
        print submission.selftext


if __name__ == '__main__':
    bot()
    arguments()
