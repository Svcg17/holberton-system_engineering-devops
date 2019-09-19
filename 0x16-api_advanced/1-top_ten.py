#!/usr/bin/python3
"""
The 1-top_ten module
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 ho
    t posts listed for a given subreddit
    """
    req = requests.get('https://www.reddit.com/r/{}.json?sort=hot&limit=10'
                       .format(subreddit),
                       headers={'User-agent': 'My User Agent 1.0'},
                       allow_redirects=False)

    try:
        list_titles = (req.json().get('data').get('children'))
        for i in list_titles:
            print(i.get('data').get('title'))
    except Exception:
        print(None)
