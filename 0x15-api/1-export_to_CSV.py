#!/usr/bin/python3
"""Export employee TODO list info to .CSV, by employee ID"""

import requests
import sys
import csv


if __name__ == "__main__":
    hostname = "https://jsonplaceholder.typicode.com"
    user = requests.get(hostname + "/users/{}".format(sys.argv[1])).json()
    userTodoList = requests.get(
        hostname + "/todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        [csvWriter.writerow(
            [sys.argv[1], user.get("username"), task.get("completed"),
             task.get("title")]) for task in userTodoList]
