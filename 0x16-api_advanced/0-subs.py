#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    function to get no of subscriber
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    header = {'User-Agent': 'My User Agent 1.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    r = requests.get(url, headers=header).json()
    subs = r.get('data', {}).get('subscribers', 0)
    return subs
