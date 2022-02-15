#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    recursive function that queries the Reddit API
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    url = {'User-Agent': 'My User Agent 1.0'}
    header = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers=header, params={'after': after}, allow_redirects=False).json()
    after = r.get('data', {}).get('after', None)
    posts = r.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
