#!/usr/bin/python3
"""Export to csv informations about an employee todo list progress"""
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    url_all = '{}users'.format(url)
    res = requests.get(url_all)
    users = res.json()
    users_dic = {}

    for user in users:
        name = user.get('username')
        userid = user.get('id')
        url_todo = '{}todos?userId={}'.format(url, userid)
        res = requests.get(url_todo)
        tasks = res.json()
        task_l = []
        for task in tasks:
            dic = {}
            dic['username'] = name
            dic["task"] = task.get('title')
            dic['completed'] = task.get('completed')
            task_l.append(dic)

        users_dic[str(userid)] = task_l
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(users_dic, f)
