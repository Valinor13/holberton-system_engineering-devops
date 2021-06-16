#!/usr/bin/python3
""" A module to convert API information to a CSV file """


import json
import requests
import sys


def save_tasks_to_json(employeeId):
    """ Get the employee tasks from API """
    username = ''
    userDict = {}

    usersRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            employeeId))
    todosRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            employeeId))
    username = usersRes.json().get('username')
    todosJson = todosRes.json()

    userDict[employeeId] = []

    for task in todosJson:
        taskDict = {}
        taskDict["task"] = task.get('title')
        taskDict["username"] = username
        taskDict["completed"] = task.get('completed')

        userDict[employeeId].append(taskDict)

    with open("{}.json".format(employeeId), 'w') as jf:
        json.dump(userDict, jf)

    return 0

if __name__ == '__main__':
    save_tasks_to_json(sys.argv[1])
