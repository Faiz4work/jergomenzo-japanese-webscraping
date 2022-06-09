import requests as r
from parsel import Selector
from math import ceil
from multiprocessing.pool import ThreadPool

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}
user_page_scrol_link_example = "https://www.jianshu.com/users/ef4f2422125f/?count=10&page=1"
posts_per_page = 9
core_link = "https://www.jianshu.com"





def get_total_post_count(link):
    res = r.get(link, headers=headers).text
    res = Selector(text=res)
    num = res.xpath("//div[@class='info']/ul/li[3]/div/a/p/text()").get()
    num = int(num)
    return num

def get_all_post_of_user(link):
    total_posts = get_total_post_count(link)
    pages = total_posts / posts_per_page
    pages = ceil(pages)
    print(f"{pages} Pages in: {link}")
    link = link.replace("users", "u")

    all_links = []

    # for i in range(1, pages+1):
    for i in range(1, pages+1):
        # print(f"Getting page no: {i}")
        aurl = link+ f"?order_by=shared_at&page={i}"
        
        res = r.get(url=aurl, headers=headers)
        page = Selector(text=res.text)

        hrefs = page.xpath("//a[@class='title']/@href").getall()
        for i in hrefs:
            abs_link = core_link + i
            all_links.append(abs_link)

    return all_links


# Adding a comment