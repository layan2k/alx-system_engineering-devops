#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import requests
from sys import argv
import json


r = requests.get('https://jsonplaceholder.typicode.com/users')
t = requests.get('https://jsonplaceholder.typicode.com/todos')


def create_json():
    """API data"""
    for item in r.json():
        if item.get('id') == int(argv[1]):
            USERN = (item.get('username'))
            break
    tstatus = []
    for stuff in t.json():
        if stuff.get('userId') == int(argv[1]):
            tstatus.append((stuff.get('completed'), stuff.get('title')))

    """export json"""
    tl = []
    for task in tstatus:
        tl.append({"task": task[1], "completed": task[0], "username": USERN})
        data = {str(argv[1]): tl}
        filename = "{}.json".format(argv[1])
        with open(filename, "w")as f:
            json.dump(data, f)


if __name__ == '__main__':
    create_json()
