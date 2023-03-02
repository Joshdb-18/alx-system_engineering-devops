#!/usr/bin/python3
""" Queries the Reddit API"""


def count_words(subreddit, word_list, word_dict=None, after=None):
    """ A function that queries the Reddit API recursively, parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """
    import requests

    if not word_dict:
        word_dict = {}

    if not after:
        url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(
                subreddit, after)

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return
    elif response.status_code != 200:
        # raise Exception(f'Error {response.status_code}')
        return None

    data = response.json()
    children = data['data']['children']
    after = data['data']['after']

    def search_child(child, word_list, word_dict):
        title = child['data']['title'].lower()

        def search_word(word, title, word_dict):
            if word.lower() in title:
                if word.lower() not in word_dict:
                    word_dict[word.lower()] = 1
                else:
                    word_dict[word.lower()] += 1

        for word in word_list:
            search_word(word, title, word_dict)

    def search_children(children, word_list, word_dict):
        if children:
            search_child(children[0], word_list, word_dict)
            search_children(children[1:], word_list, word_dict)

    search_children(children, word_list, word_dict)

    if after:
        count_words(subreddit, word_list, word_dict, after)
    else:
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))

        def print_word_count(sorted_words):
            if sorted_words:
                word, count = sorted_words[0]
                print('{}: {}'.format(word, count))
                print_word_count(sorted_words[1:])

        print_word_count(sorted_words)
