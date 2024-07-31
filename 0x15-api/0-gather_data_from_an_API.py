#!/usr/bin/python3
"""Return employee TODO list progress, by employee ID"""

import requests
import sys


if __name__ == "__main__":
    hostname = "https://jsonplaceholder.typicode.com"
    user = requests.get(hostname + "/users/{}".format(sys.argv[1])).json()
    userTodoList = requests.get(
        hostname + "/todos", params={"userId": sys.argv[1]}).json()

    completedTasks = [task.get(
        "title") for task in userTodoList if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completedTasks), len(userTodoList)))
    [print("\t {}".format(task)) for task in completedTasks]
