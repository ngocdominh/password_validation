# Implement a URL shortener with the following methods:
#
# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
# Hint: What if we enter the same URL twice?


# - a dictionary which saves uid and the relative url
# - regular url => return shortened url
# - shortened url => regular url or None


import string
import random

url_dict = {}


def shorten():
    i = 0
    alnum = string.ascii_lowercase + string.ascii_uppercase + string.digits
    ori_url = input('Original URL: ')
    gen_char = random.choices(alnum, k=6)
    short_url = ''.join(gen_char)

    # if key exists in dict, pass; otherwise, add key-value pair to dict
    # limit length of characters between 5 ('http...') and 2048 (the maximum length of a URL)
    if len(ori_url) > 2048 or len(ori_url) < 5:
        print("Invalid URL")
    elif short_url in url_dict.keys():
        pass
    else:
        url_dict[short_url] = ori_url
        i += 1
    print("The short version is: " + short_url)


def restore():
    short_url = input('Shorten URL: ')
    if len(short_url) != 6 or short_url not in url_dict.keys():
        print("Invalid shortened URL")
        return None
    else:
        print("The original URL is: " + url_dict[short_url])


shorten()
restore()
