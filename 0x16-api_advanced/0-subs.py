#!/usr/bin/python3
"""
The 0-subs module
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    for a given subrredit
    """
    req = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers={'User-agent': 'your bot 0.1'},
                       allow_redirects=False)
    try:
        subs = (req.json().get('data').get('subscribers'))
        return (subs)
    except ValueError:
        return (0)
