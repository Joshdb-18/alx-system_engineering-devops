#!/usr/bin/python3
""" Queries the Reddit API"""


import requests


def count_words(subreddit, word_list, word_dict=None, after=None):
    """ A function that queries the Reddit API recursively, parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """

    if not word_dict:
        word_dict = {}

    if not after:
        url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot/.json?after={after}'

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return
    if response.status_code != 200:
        # raise Exception(f'Error {response.status_code}')
        return None

    data = response.json()
    children = data['data']['children']
    after = data['data']['after']

    for child in children:
        title = child['data']['title'].lower()

        for word in word_list:
            if word.lower() in title:
                if word.lower() not in word_dict:
                    word_dict[word.lower()] = 1
                else:
                    word_dict[word.lower()] += 1

    if after:
        count_words(subreddit, word_list, word_dict, after)
    else:
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_words:
            print(f'{word}: {count}')
