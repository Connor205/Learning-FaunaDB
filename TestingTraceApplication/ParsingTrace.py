from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import get_passwords
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(os.environ['SELENIUM_DRIVER'],
                          options=chrome_options)

driver.get("https://www.applyweb.com/eval/shibboleth/neu/36892")

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys("nelson.co")
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(get_passwords.getMyNortheastern())
login_button = driver.find_element_by_xpath(
    "/html/body/section/div/div[1]/div/form/div[3]/button")
login_button.click()
input()
driver.get(
    "https://www.applyweb.com/eval/resources/js/reportbrowser/reportbrowser.html"
)
time.sleep(5)
# print(driver.page_source)
container = driver.find_element_by_id("tapestryContainer")
summer_2_2020 = container.find_element_by_css_selector(
    "#TermSelect > option:nth-child(4)")
summer_2_2020.click()
time.sleep(5)
college_of_eng = container.find_element_by_css_selector(
    "#SchoolSelect > option:nth-child(6)")
college_of_eng.click()
view_all = container.find_element_by_css_selector(
    "#tapestryContainer > div > div:nth-child(1) > div.col-sm-12 > form > a")
view_all.click()
time.sleep(3)

container.find_element_by_css_selector(
    "#tapestryContainer > div.modal.ng-isolate-scope.in > div > div > div.modal-footer.ng-scope > button:nth-child(1)"
).click()
time.sleep(10)
links_elm = container.find_elements_by_tag_name("a")
links = [x.get_attribute("href") for x in links_elm]
print(links)

input()
driver.close()
