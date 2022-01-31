#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import requests
from sys import argv
import json

users = requests.get('https://jsonplaceholder.typicode.com/users')
todos = requests.get('https://jsonplaceholder.typicode.com/todos')


def tojson():
    """API data"""
    for u in users.json():
        if u.get('id') == int(argv[1]):
            USERNAME = (u.get('username'))
            break
    TASK_STATUS_TITLE = []
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """export json"""
    t = []
    for task in TASK_STATUS_TITLE:
        t.append({"task": task[1], "completed": task[0], "username": USERNAME})
    data = {str(argv[1]): t}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    tojson()
