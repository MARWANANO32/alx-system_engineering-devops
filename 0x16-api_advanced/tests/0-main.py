#!/usr/bin/python3
""" Main file """

import sys

if __name__ == "__main__":
    number_of_subcribers = __import__('0-subs').number_of_subcribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
