#!/usr/bin/python3
"""Querrying the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Querry a subreddit and retrieve number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user-agent": "My user agent 1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
