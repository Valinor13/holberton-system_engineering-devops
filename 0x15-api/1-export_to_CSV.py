#!/usr/bin/python3
""" A module to convert API information to a CSV file """


import requests
import csv
import sys


def get_employee_tasks(employeeId):
    """ Get the employee tasks from API """
    name = ''
    task_list = []

    usersRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            employeeId))
    todosRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            employeeId))
    name = usersRes.json().get('name')
    todosJson = todosRes.json()

    for task in todosJson:
        taskRow = []
        taskRow.append(employeeId)
        taskRow.append(name)
        taskRow.append(task.get('completed'))
        taskRow.append(task.get('title'))
        task_list.append(taskRow)

    with open("{}.csv".format(employeeId), 'w') as cf:
        csvwriter = csv.writer(cf, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(task_list)

    return 0

if __name__ == '__main__':
    get_employee_tasks(sys.argv[1])
