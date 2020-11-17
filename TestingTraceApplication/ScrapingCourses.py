from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
import json

baseLink = "http://catalog.northeastern.edu/"
main_page = requests.get(baseLink + "course-descriptions/")
main_page_soup = BeautifulSoup(main_page.content, 'html.parser')
linkAttributes = main_page_soup.find_all('a')

<<<<<<< HEAD
pageLinks = []
departments = []
for link in linkAttributes:
    if link.has_attr("href"):
        l = link['href']
        if "/course-descriptions/" in l:
            #print(l)
            name = link.text
            #print(l[21:-1])
            #print(name)
            pageLinks.append(l)
            departments.append(link.text)

all_classes = {}
for index, link in enumerate(pageLinks):
    print(baseLink + link)
    page = requests.get(baseLink + link)
    page_soup = BeautifulSoup(page.content, 'html.parser')
    # print(page_soup.prettify)
    class_headers = [
        x.text.replace("\xa0", "").split(".")[:-1]
        for x in page_soup.find_all("p", {"class": "courseblocktitle"})
    ]
    descriptions = [
        x.text.replace("\n", "")
        for x in page_soup.find_all("p", {"class": "courseblockdesc"})
    ]
    for i in range(len(class_headers)):
        all_classes[class_headers[i][0]] = {
            "name": class_headers[i][1][2:],
            "credit_hours": class_headers[i][2][2:]
            # "description": descriptions[i]
        }

with open("classes_no_desc.txt", "w+") as ouputfile:
    json.dump(all_classes, ouputfile)

# print(links)
# print(main_page_soup.prettify())
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# print(os.environ['SELENIUM_DRIVER'])
# driver = webdriver.Chrome(os.environ['SELENIUM_DRIVER'],
#                           options=chrome_options)

# driver.get("http://catalog.northeastern.edu/course-descriptions/")
# link1 = driver.find_element_by_xpath("//*[@id='atozindex']/ul[1]/li[2]/a")
# link1 = link1.get_attribute("href")
# print(link1)
=======
driver.get("http://catalog.northeastern.edu/course-descriptions/")
link1 = driver.find_element_by_xpath("//*[@id='atozindex']/ul[1]/li[2]/a")
link1 = link1.get_attribute("href")
print(link1)
>>>>>>> 1169343e392735fc7f16ed014806895339a83138
