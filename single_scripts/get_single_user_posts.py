from get_all_posts import get_all_post_of_user
import requests as r
from threading import Thread
from time import sleep
from math import ceil
from parsel import Selector


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}
core_link = "https://www.jianshu.com"

c = 1

def start_post_saving(link, dir_name):
    global c
    res = r.get(link, headers=headers).text
    sel = Selector(text=res)
    title = sel.xpath("//h1/text()").get()
    if title is not None:
        title = title.replace("|", " ")
        title = title.replace("，", " ")
        title = title.replace("?", " ")
        title = title.replace("\"", " ")
        title = title.replace("/", " ")
        title = title.replace("-", " ")
    article = sel.xpath("//article/p/text()").getall()
    a = open(f"{dir_name}/{title}.txt", 'w', encoding='utf-8')
    for line in article:
        a.write(line + '\n')
    a.close()
    print(f"{c} Posts Saved!")
    c += 1


def get_posts_link():
    # Reading user profile link
    # link = "https://www.jianshu.com/c/3sT4qY"
    # core_url = "https://www.jianshu.com/c/3sT4qY?order_by=added_at&page="
    
    link = "https://www.jianshu.com/c/bDHhpK"
    core_url = "https://www.jianshu.com/c/bDHhpK?order_by=added_at&page="

    # getting all users post
    total_posts = 110215
    pages = total_posts / 9
    pages = ceil(pages)
    print(f"{pages} Pages in: {link}")
    
    for i in range(1, pages+1):
        abs_link = core_url + str(i)
        res = r.get(url=abs_link, headers=headers)
        page = Selector(text=res.text)

        hrefs = page.xpath("//a[@class='title']/@href").getall()
        for i in hrefs:
            abs_link2 = core_link + i
            t = Thread(target=start_post_saving, args=[abs_link2, 'u2' ])
            t.start()
            
        

get_posts_link()
