#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import requests
from sys import argv
import json


userss = requests.get('https://jsonplaceholder.typicode.com/users')
todos = requests.get('https://jsonplaceholder.typicode.com/todos')


def alljson():
    """return API data"""
    USERS = []
    for u in userss.json():
        USERS.append((u.get('id'), u.get('username')))
    TASK_STATUS_TITLE = []
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))

    """export to json"""
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    alljson()
