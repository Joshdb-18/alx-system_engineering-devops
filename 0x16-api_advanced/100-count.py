#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """A function that queries the Reddit API parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {"User-Agent": "reddit-client"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return

    articles = response.json()["data"]["children"]
    last_article = articles[-1]["data"] if articles else None
    current_counts = counts.copy()

    for article in articles:
        title = article["data"]["title"].lower()
        title_words = [word.strip("!.,_") for word in title.split()]

        for keyword in word_list:
            if keyword.lower() in title_words:
                current_counts[keyword.lower()] = (
                    current_counts.get(keyword.lower(), 0) + 1
                )

    if last_article:
        return count_words(subreddit, word_list,
                           last_article["name"], current_counts)

    sorted_counts = sorted(current_counts.items(), key=lambda x: (-x[1], x[0]))
    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
