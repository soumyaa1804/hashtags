import re

# From https://github.com/hatnote/hashtag-search/blob/1e02506a732b3e018521c431c4b5c3f3c0618215/common.py
EXCLUDED = ('redirect',
            'weiterleitung',
            'redirection',
            'ifexist',
            'switch',
            'ifexpr',
            'if',
            'rs')


def hashtag_match(comment):
	# From https://gist.github.com/mahmoud/237eb20108b5805aed5f
	hashtag_re = re.compile("(?:^|\s)[＃#]{1}(\w+)")

	return hashtag_re.findall(comment)


def valid_hashtag(hashtag):

    not_excluded = hashtag.lower() not in EXCLUDED
    not_only_numbers = not hashtag.isdigit()

    return all([not_excluded, not_only_numbers])


def valid_edit(change):

    # Exclude Wikidata for now, just far too much data
    project_match = change['meta']['domain'] != "www.wikidata.org"

    # Excluding bots, mostly because of IABot. Lots of data, not very useful.
    not_bot = not change['bot']

    return all([project_match, not_bot])