#!/usr/bin/python3
"""Returns informations about an employee todo list progress"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    url_id = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(url_id)
    user = res.json()
    print("Employee {} is done with tasks".format(user.get('name')),
          end="")

    url_todo = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(url_todo)
    tasks = res.json()
    task_c = []
    for task in tasks:
        if task.get('completed'):
            task_c.append(task)

    print("({}/{}):".format(len(task_c), len(tasks)))
    for task in task_c:
        print("\t {}".format(task.get("title")))
