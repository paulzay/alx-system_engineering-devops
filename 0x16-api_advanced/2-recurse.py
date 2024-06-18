#!/usr/bin/python3
"""recursion"""

import requests


def recurse(subreddit, hot_list=[]):
    """docs"""
    r = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "Custom-User-Agent"},
                            allow_redirects=False)
    if r.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in r.json()
                        .get("data")
                        .get("children")]

    info = r.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
