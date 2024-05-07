#!/usr/bin/python3
"""
Recursively querying the Reddit API
"""
import requests

def recurse(subreddit, hot_list=[]):
    """
    A function to recursively query the Reddit API to retrieve titles of
    all hort articles for a given subreddit.

    Args: 
    subreddit: A string representing the namd of the subreddit.
    hot_list: A list to store the titles of the hot articles. Default is
              any empty list.

    Return:
    - A list with titles of all the hot articles for a given subreddit.
    - None, if no results are found.
    """

    url: "https://www.reddit.com/r/{subreddit}/hot.json".format(subreddit)
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
