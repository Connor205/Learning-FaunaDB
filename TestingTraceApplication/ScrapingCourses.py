from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(os.environ['SELENIUM_DRIVER'],
                          options=chrome_options)

testing = 5

driver.get("http://catalog.northeastern.edu/course-descriptions/")
link1 = driver.find_element_by_xpath("//*[@id='atozindex']/ul[1]/li[2]/a")
link1 = link1.get_attribute("href")
print(link1)