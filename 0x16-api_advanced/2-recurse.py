#!/usr/bin/python3
""" Defines a recursive function to query titles of all hot articles
on a subreddit from the Reddit API"""

from requests import get
after = None


def recurse(subreddit, hot_list=[]):
    """queries the all articles title"""
    global after

    if not isinstance(subreddit, str) or not subreddit:
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': after}
    user_agent = {'User-agent': 'Google Chrome Version 117.0.5938.132'}
    response = get(url, headers=user_agent, params=params,
                   allow_redirects=False)

    if response.status_code == 200:
        res = response.json()
        after_data = res.get('data').get("after")
        if after_data:
            after = after_data
            recurse(subreddit, hot_list)
        all_children = res.get("data").get("children")
        for child in all_children:
            hot_list.append(child.get('data').get('title'))

        return hot_list

    return None
