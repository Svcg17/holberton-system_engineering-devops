#!/usr/bin/python3
"""
The 2-recurse module
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    req = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after),
                       headers={'User-agent': 'My User Agent 1.0'},
                       allow_redirects=False)
    if req.status_code != 200:
        return None
    if after is None:
        return hot_list

    for i in req.json().get('data').get('children'):
        hot_list.append(i.get('data').get('title'))

    after = req.json().get('data').get('after')
    recurse(subreddit, hot_list, after)
    return(hot_list)
