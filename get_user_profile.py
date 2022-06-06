from numpy import absolute
import requests as r
from parsel import Selector

base_url = "https://www.jianshu.com/recommendations/users?page="
core_url = "https://www.jianshu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}

last_page = 100

# Getting first page
result = r.get(url=base_url + '1', headers=headers)
# print(result.text)



res = Selector(text=result.text)
user_endpoints = res.xpath("//div[@class='wrap']/a/@href").getall()
# print(user_endpoints)
absolute_user_profiles = [core_url + i for i in user_endpoints]
print(absolute_user_profiles)

with open("user_profiles.txt", 'w') as f:
    for i in absolute_user_profiles:
        f.write(i + '\n')
    

# for i in range(1, last_page+1):
#     result = r.get(url=base_url + str(i), headers=headers)
    # print(result)



