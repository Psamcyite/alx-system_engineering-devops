#!/usr/bin/python3
"""This module contains the number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "UserX"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        sub_number = data["data"]["subscribers"]
        return sub_number
    else:
        return 0
