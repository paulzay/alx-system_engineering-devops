#!/usr/bin/python3
"""subs count"""
import requests


def number_of_subscribers(subreddit):
    """use reddit api"""
    r = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                      headers={"User-Agent": "Custom-User-Agent"},)
    if r.status_code != 200:
        return 0

    return r.json().get('data').get('subscribers')
