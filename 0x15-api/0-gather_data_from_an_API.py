#!/usr/bin/python3
"""By using a REST API, for a given employee ID, returns information about
his/her TODO list progress
"""
if __name__ == "__main__":
    from sys import argv
    import requests

    completed = 0
    total_t = 0
    titles = []
    req_id = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))
    req = requests.get('https://jsonplaceholder.typicode.com/todos/')
    name = (req_id.json().get('name'))
    r_json = req.json()
    for i in r_json:
        if i.get('userId') == int(argv[1]):
            if i.get('completed') is True:
                titles.append(i.get('title'))
                completed += 1
            total_t += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_t))
    for i in titles:
        print("     {}".format(i))
