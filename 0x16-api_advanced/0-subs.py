#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    function to get no of subscriber
    """
    if type(subreddit) is not str or subreddit is None:
        return 0

    header = requests.utils.default_headers()
    header.update({'User-Agent': 'My User Agent 1.0'})
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    r = requests.get(url, headers=header).json()
    subs = r.get('data', {}).get('subscribers')
    return subs
