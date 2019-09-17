#!/usr/bin/python3
"""
Using what is done in task #0, exports data in the CSV format
"""
if __name__ == "__main__":
    import csv
    from sys import argv
    import requests

    filename = argv[1] + ".csv"
    req = requests.get('https://jsonplaceholder.typicode.com/todos/')
    req_id = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))
    name = (req_id.json().get('username'))
    with open(filename, "w") as f:
        r_json = req.json()
        for i in r_json:
            if i.get('userId') == int(argv[1]):
                w = csv.writer(f, quoting=csv.QUOTE_ALL)
                w.writerow([i.get('userId'), name,
                           i.get('completed'), i.get('title')])
