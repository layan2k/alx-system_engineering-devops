#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import requests
from sys import argv
import json


r = requests.get('https://jsonplaceholder.typicode.com/users')
t = requests.get('https://jsonplaceholder.typicode.com/todos')


def alljson():
    """API data"""
    US = []
    for items in r.json():
        US.append((items.get('id'), items.get('username')))
    statustask = []
    for stuff in t.json():
        statustask.append((stuff.get('userId'),
                           stuff.get('completed'),
                           stuff.get('title')))

    """export json"""
    data = dict()
    for u in US:
        tl = []
        for task in statustask:
            if task[0] == u[0]:
                tl.append({"task": task[2],
                           "completed": task[1],
                           "username": u[1]})

        data[str(u[0])] == tl
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == '__main__':
    alljson()
