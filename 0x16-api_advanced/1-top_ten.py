#!/usr/bin/python3
"""This module contains the top_ten function"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "UserX"}
    response = requests.get("{}?limit={}".format(url, 10), headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(post.get('data').get('title'))
    else:
        print(None)
