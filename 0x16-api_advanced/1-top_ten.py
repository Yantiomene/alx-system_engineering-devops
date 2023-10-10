#!/usr/bin/python3
""" Defines a function to request the top ten post
on a subreddit from the Reddit API"""

from requests import get


def top_ten(subreddit):
    """queries the top ten posts title"""
    if not isinstance(subreddit, str) or not subreddit:
        print("None")

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'limit': 10}
    user_agent = {'User-agent': 'Google Chrome Version 117.0.5938.132'}
    response = get(url, headers=user_agent, params=params)
    res = response.json()

    try:
        children = res.get('data').get('children')
        for child in children:
            print(child.get('data').get('title'))
    except Exception:
        print("None")
