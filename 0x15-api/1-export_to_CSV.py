#!/usr/bin/python3
"""
Using what is in the task #0, extend your Python script to export
data in the CSV forma
"""


import requests
from sys import argv
import csv


if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(userId), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])