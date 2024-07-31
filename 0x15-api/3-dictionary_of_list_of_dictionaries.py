#!/usr/bin/python3
"""Export TODO list info of all employees to .JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    hostname = "https://jsonplaceholder.typicode.com"
    users = requests.get(hostname + "/users").json()

    with open("todo_all_employees.json", "w", newline="") as jsonFile:
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed"),
        } for task in requests.get(
            hostname + "/todos", params={"userId": user.get("id")}).json()
        ] for user in users}, jsonFile)
