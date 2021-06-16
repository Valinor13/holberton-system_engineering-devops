#!/usr/bin/python3
""" A module to convert API information to a CSV file """


import json
import requests


if __name__ == '__main__':
    def save_tasks_to_json():
        """ Get the employee tasks from API """
        dic = {}

        user_json = requests.get(
            'https://jsonplaceholder.typicode.com/users/').json()
        todos_json = requests.get(
            'https://jsonplaceholder.typicode.com/todos/').json()

        user_info = {}
        for user in user_json:
            user_info[user['id']] = user['username']

        for task in todos_json:
            if dic.get(task['userId'], False) is False:
                dic[task['userId']] = []
            task_dict = {}
            task_dict['username'] = user_info[task['userId']]
            task_dict['task'] = task['title']
            task_dict['completed'] = task['completed']
            dic[task['userId']].append(task_dict)

        fn = "todo_all_employees.json"
        with open(fn, 'w') as jf:
            json.dump(dic, jf)
