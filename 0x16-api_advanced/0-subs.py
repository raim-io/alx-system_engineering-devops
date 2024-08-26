#!/usr/bin/python3
"""REDDIT API: Fetch number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Fetch the number of subscribers off a subredidt"""

    req = requests.get(
        "https://www.reddit.com/r/{}/about.json"
        .format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get('data').get('subscribers')
    else:
        return 0
