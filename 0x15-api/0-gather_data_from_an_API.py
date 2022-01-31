#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her 2DO list progress
"""

import requests
from sys import argv

r = requests.get('https://jsonplaceholder.typicode.com/users')
t = requests.get('https://jsonplaceholder.typicode.com/todos')


def get_items():
    """get Api data n return"""
    for item in r.json():
        if item.get('id') == int(argv[1]):
            namev = (item.get('name'))
            break
    notasks = 0
    totaltasks = 0
    tasksname = []
    for stuff in t.json():
        if stuff.get('userId') == int(argv[1]):
            totaltasks += 1
            if stuff.get('completed') is True:
                notasks += 1
                tasksname.append(stuff.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(namev,
                                                          notasks, totaltasks))

    for task in tasksname:
        print("\t {}".format(task))


if __name__ == '__main__':
    get_items()
