#!/usr/bin/python3
"""
function that queries the Reddit API and
prints the titles of the first 10 hot
posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    """
    function ti=o query the Reddit API
    """
    if type(subreddit) is not str or  subreddit is None:
        print(None)
    header = requests.utils.default_headers()
    header.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
                      headers=header).json()

    ten = r.get(('data', {}).get('children', []))

    return ten
