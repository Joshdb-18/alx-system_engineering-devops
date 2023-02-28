#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests


def count_words(subreddit, word_list, after=None, counts={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "reddit-client"}

    if after:
        url += f"&after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(f"Error: Invalid subreddit or no posts found.")
        return

    data = response.json()["data"]
    articles = data["children"]
    last_article = articles[-1]["data"] if articles else None

    for article in articles:
        title = article["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            if (
                f" {word} " in f" {title} "
                or f" {word}," in f" {title} "
                or f" {word}." in f" {title} "
                or f" {word}!" in f" {title} "
                or f" {word}?" in f" {title} "
            ):
                counts[word] = counts.get(word, 0) + 1

    if last_article:
        return count_words(subreddit, word_list, last_article["name"], counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")
