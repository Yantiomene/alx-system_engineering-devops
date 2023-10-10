#!/usr/bin/python3
""" Defines a recursive function to query titles of all hot articles
and prints a sorted count of a given keywords
on a subreddit from the Reddit API"""

from requests import get


def count_words(subreddit, word_list, after="", count=[]):
    """queries the all articles title"""
    if after == "":
        count = [0] * len(word_list)

    if not isinstance(subreddit, str) or not subreddit:
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': after}
    user_agent = {'User-agent': 'Google Chrome Version 117.0.5938.132'}
    response = get(url, headers=user_agent, params=params,
                   allow_redirects=False)

    if response.status_code == 200:
        res = response.json()
        for child in res.get('data').get('children'):
            for word in child.get('data').get('title').split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = res.get('data').get("after")
        if after:
            count_words(subreddit, word_list, after, count)
        else:
            index_save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower == word_list[j].lower():
                        index_save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                        (count[i] == count[j] and
                         word_list[i] > word_list[j])):
                        count[i], count[j] = count[j], count[i]
                        tmp = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = tmp
            for i in range(len(word_list)):
                if (count[i] > 0 and i not in index_save):
                    print("{}: {}".format(word_list[i].lower(), count[i]))
