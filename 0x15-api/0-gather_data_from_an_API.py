#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    usr = requests.get("{}/users/{}".format(url, sys.argv[1])).json()
    todos = requests.get("{}/todos?userId={}".format(url, sys.argv[1])).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        usr.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
