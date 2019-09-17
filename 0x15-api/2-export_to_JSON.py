#!/usr/bin/python3
"""
Using what is done in task #0, exports data in the CSV format
"""
if __name__ == "__main__":
    import json
    from sys import argv
    import requests

    newd = {}
    filename = argv[1] + ".json"
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(argv[1]))
    req_id = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))
    name = (req_id.json().get('username'))
    with open(filename, "w") as f:
        r_json = req.json()
        d = [{'task': i.get('title'), 'completed': i.get('completed'),
              'username': name}for i in r_json]
        newd[argv[1]] = d
        json.dump(newd, f)
