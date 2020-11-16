import requests
import json
import pprint as pp
from bs4 import BeautifulSoup as bs

with open("khoury_links.txt", "r") as link_file:
    links = json.load(link_file)

test = open("test.txt", "w+")

# print(links)

for link in links[:1]:
    page = requests.get(link)
    page_soup = bs(page.content, 'html.parser')
    info_soup = page_soup.find_all("div", class_="copy paragraph")[-1]
    headers = [h.string for h in info_soup.find_all("h2")]
    print(headers)
    contents = [x for x in info_soup.contents if x != "\n"]
    # print(contents)
