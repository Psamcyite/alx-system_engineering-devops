#!/usr/bin/python3
"""This module contains the recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "UserX"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get("data").get("after")
        if posts is not None:
            after = posts
            recurse(subreddit, hot_list, after)
            titles = response.json().get("data").get("children")
            for title in titles:
                hot_list.append(title.get("data").get("title"))
            return hot_list
        else:
            return (None)
