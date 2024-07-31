#!/usr/bin/python3
"""Export employee TODO list info to .JSON, by employee ID"""

import json
import requests
import sys


if __name__ == "__main__":
    hostname = "https://jsonplaceholder.typicode.com"
    user = requests.get(hostname + "/users/{}".format(sys.argv[1])).json()
    userTodoList = requests.get(
        hostname + "/todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(sys.argv[1]), "w", newline="") as jsonFile:
        json.dump({sys.argv[1]: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in userTodoList]}, jsonFile)
