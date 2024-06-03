#!/usr/bin/python3
# fetch

import requests
import sys

if __name__ == "__main__":
    argv = sys.argv[1]
    try:
        req = requests.get('https://jsonplaceholder.typicode.com/todos/')
        req2 = requests.get('https://jsonplaceholder.typicode.com/users/')

        todos = req.json()
        users = req2.json()

        total_tasks = 0
        done_tasks = 0
        tasks = []
        uname = ''
        for todo in todos:
            if todo.get('userId') == int(argv):
                for user in users:
                    if user.get('id') == int(argv):
                        uname = user.get('name')
                total_tasks+=1
                if todo.get('completed') == True:
                    tasks.append(todo)
                    done_tasks+=1
        print(f"Employee {uname} is done with tasks ({done_tasks}/{total_tasks}):")
        for task in tasks:
            print(f"     {task.get('title')}")
    except Exception as e:
        raise e
