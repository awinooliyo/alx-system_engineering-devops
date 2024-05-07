#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list containing the titles of all
    hot articles for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.
    hot_list (list, optional): A list to store the titles of the hot articles.
                               Default is an empty list.
    after (str, optional): A token to paginate through the results.
                           Default is an empty string.
    count (int, optional): The count of posts fetched so far. Default is 0.

    Returns:
    list: A list containing the titles of all hot articles
          for the given subreddit.
          None if no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
