#!/usr/bin/python3
"""
Querrying Reddit API
"""
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.

    Args: A string representing the name of the subreddit.

    Returns:
    - The titles of the to 10 hot posts listed for a given subreddit.
    - O or None if inbalid subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
