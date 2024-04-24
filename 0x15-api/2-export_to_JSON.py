#!/usr/bin/python3
"""Export data to JSON"""
import json
import requests
import sys

if __name__ == "__main__":
    usr_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, usr_id)).json()
    username = user.get("username")
    todos = requests.get("{}/todos?userId={}".format(url, usr_id)).json()

    with open("{}.json".format(usr_id), "w") as jsonfile:
        json.dump({usr_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todos]}, jsonfile)
