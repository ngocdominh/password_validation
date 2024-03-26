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
    ori_url = input('Original URL: ')
    alnum = string.ascii_lowercase + string.ascii_uppercase + string.digits
    gen_char = random.choices(alnum, k=6)
    short_url = ''.join(gen_char)

    # if key exists in dict, pass; otherwise, add key-value pair to dict

    if short_url in url_dict.keys():
        pass
    else:
        url_dict[short_url] = ori_url


def restore():
    short_url = input('Shorten URL: ')
    if short_url not in url_dict.keys():
        return None
    else:
        print("The original URL is: " + url_dict[short_url])


# alnum = string.ascii_lowercase + string.ascii_uppercase + string.digits
#
# for i in range(2):
#     ori_url = input('Original URL: ')
#     gen_char = random.choices(alnum, k=6)
#     short_url = ''.join(gen_char)
#
# # if key exists in dict, pass; otherwise, add key-value pair to dict
#
#     if short_url in url_dict.keys():
#         pass
#     else:
#         url_dict[short_url] = ori_url
#     print(short_url)
#     print(url_dict)
#
#
# short_url = input('Shorten URL: ')
# if short_url not in url_dict.keys():
#     print("No url available")
# else:
#     print("The original URL is: " + url_dict[short_url])
