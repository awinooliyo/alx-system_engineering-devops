#!/usr/bin/python3
"""
Querrying the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and retrieves
    number of subscribers for a given subreddit

    Args:
    - subreddit: A string representing the name of the subreddit

    Returns:
    - An integer representing the number of subscribers
    - 0 if the subreddit id invalid or inexistent
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My User Agent 1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        if not data:
            return 0
        subscribers = data.get("subscribers", 0)
        return subscribers
    else:
        return 0
