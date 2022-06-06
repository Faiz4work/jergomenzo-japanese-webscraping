import requests as r
from parsel import Selector
from .get_all_posts import get_all_post_of_user

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}

f = open("user_profiles.txt", 'r')

user_links = [i.strip() for i in f.readlines()]

f.close()
# print(user_links)

# getting a single user's post
all_posts_link = get_all_post_of_user(user_links[0])



