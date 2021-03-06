import requests as r
from parsel import Selector
from threading import Thread
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}

def start_post_saving(link, dir_name):
    res = r.get(link.strip(), headers=headers).text
    sel = Selector(text=res)
    title = sel.xpath("//h1/text()").get()
    if title is not None:
        title = title.replace("|", "")
        title = title.replace("，", "")
        title = title.replace("?", "")
    article = sel.xpath("//article/p/text()").getall()
    a = open(f"{dir_name}/{title}.txt", 'w', encoding='utf-8')
    for line in article:
        a.write(line + '\n')
    a.close()


def save_all_posts(dir_name, txt_file):
    # Open post links file and reading it.
    f = open(txt_file, 'r')
    links = f.readlines()
    f.close

    counter = 1
    # Looking through all links
    for link in links:
        t = Thread(target=start_post_saving, args=[link, dir_name])
        t.start()
        print(f"{counter} posts saved!")
        counter  += 1
        sleep(0.1)
        



