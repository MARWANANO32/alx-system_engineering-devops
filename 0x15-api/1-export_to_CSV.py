#!/usr/bin/python3
"""Export data to CSV"""
import csv
import requests
import sys

if __name__ == "__main__":
    usr_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, usr_id)).json()
    username = user.get("username")
    todos = requests.get("{}/todos?userId={}".format(url, usr_id)).json()

    with open("{}.csv".format(usr_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [usr_id, username, t.get("completed"), t.get("title")])
         for t in todos]
