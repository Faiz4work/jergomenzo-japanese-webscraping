from get_all_posts import get_all_post_of_user
import requests as r
from threading import Thread
from time import sleep


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}


def fetch_post(link):
    all_posts_link = get_all_post_of_user(link)
    print(len(all_posts_link))
    # Appending all posts link to a .txt file:
    with open("all_users_post_link.txt", 'a') as f:
        for i in all_posts_link:
            f.write(i + '\n')


def get_posts_link():
    # Reading user profile links, approx 2400+
    f = open("user_profiles.txt", 'r')
    user_links = [i.strip() for i in f.readlines()]
    f.close()


    # getting all users post
    for link in user_links:
        t = Thread(target=fetch_post, args=[link,])
        t.start()
        sleep(1)
        

get_posts_link()
