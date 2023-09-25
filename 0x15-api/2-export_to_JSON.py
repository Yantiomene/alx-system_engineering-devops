#!/usr/bin/python3
"""Export to csv informations about an employee todo list progress"""
import json
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
        dic = {}
        dic["task"] = task.get('title')
        dic['completed'] = task.get('completed')
        dic['username'] = name
        task_l.append(dic)

    user_data = {str(sys.argv[1]): task_l}
    filename = '{}.json'.format(sys.argv[1])
    with open(filename, mode='w') as f:
        json.dump(user_data, f)
