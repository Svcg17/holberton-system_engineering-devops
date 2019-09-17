#!/usr/bin/python3
"""
By using task #0, exports data in the JSON format
"""
if __name__ == "__main__":
    import json
    from sys import argv
    import requests

    newd = {}
    user_id = {}
    filename = "todo_all_employees.json"
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    req_id = requests.get('https://jsonplaceholder.typicode.com/users/')
    with open(filename, "w") as f:
        d = {j.get("id"): [{'task': i.get('title'),
             'completed': i.get('completed'),
                            'username': j.get('username')} for i in req.json()
                           if j.get("id") == i.get('userId')]
             for j in req_id.json()}
        json.dump(d, f)
