#!/usr/bin/python3
"""Export to csv informations about an employee todo list progress"""
import csv
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    url_id = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(url_id)
    user = res.json()
    name = user.get('username')

    url_todo = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(url_todo)
    tasks = res.json()
    task_l = []
    for task in tasks:
        task_l.append([sys.argv[1], name,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(sys.argv[1])
    with open(filename, mode='w') as f:
        fw = csv.writer(f, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_ALL)

        for task in task_l:
            fw.writerow(task)
