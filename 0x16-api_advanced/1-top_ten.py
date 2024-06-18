#!/usr/bin/python3
"""task 1"""
import requests


def top_ten(subreddit):
    r = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                     .format(subreddit),
                     headers={"User-Agent": "Custom-User-Agent"},)

    if r.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in r.json().get("data").get("children")]
