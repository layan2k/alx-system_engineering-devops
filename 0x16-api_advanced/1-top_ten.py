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
    if subreddit is None or type(subreddit) is not str:
        print(None)
    header = {'User-Agent': 'My User Agent 1.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    r = requests.get(url, headers=header, params={'limit': 10}).json()

    ten = r.get(('data', {}).get('children', None))

    if ten is None or (len(ten) > 0 and ten[0].get('kind') != 't3'):
        print(None)
    else:
        for post in ten:
            print(post.get('data', {}).get('title', None))
