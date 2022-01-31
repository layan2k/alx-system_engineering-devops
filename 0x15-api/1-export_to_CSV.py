#!/usr/bin/python3
"""
Using what is in the task #0, extend your Python script to export
data in the CSV forma
"""


import requests
from sys import argv
import csv


r = requests.get('https://jsonplaceholder.typicode.com/users')
t = requests.get('https://jsonplaceholder.typicode.com/todos')


def cvrtcsv():
    """API data"""
    for item in r.json():
        if item.get('id') == int(argv[1]):
            USERN = (item.get('username'))
            break
    tstatus = []
    for stuff in t.json():
        if stuff.get('userId') == int(argv[1]):
            tstatus.append((stuff.get('completed'), stuff.get('title')))

    """ export csv"""
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldsn = ["USER_ID", "USERNAME",
                   "TASK_COMPLETED_STATUS",
                   "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldsn,
                                quoting=csv.QUOTE_NONE)

        for task in tstatus:
            writer.writerow({"USER_ID": argv[1],
                             "USERNAME": USERN,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == '__main__':
    cvrtcsv()
