#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    todos = requests.get("{}/todos".format(url)).json()

    user_dict = {}
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        for todo in todos:
            if todo.get("userId") == user_id:
                user_dict[user_id].append({
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_dict, jsonfile)
