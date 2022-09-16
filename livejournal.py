from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.livejournal.com/')
time.sleep(3)

body=driver.find_element("xpath", '//*[@id="js"]/body/div[2]/header/div[1]/nav[2]/ul/li[2]/a')
body.click()


search_box1=driver.find_element("xpath",'//*[@id="user"]')
search_box1.send_keys('syneltest')
search_box2=driver.find_element("xpath",'//*[@id="lj_loginwidget_password"]')
search_box2.send_keys('123qweASD')
body2=driver.find_element("xpath", '//*[@id="js"]/body/div[2]/div[3]/div/div[2]/form[1]/button')
body2.click()
time.sleep(3)

driver.quit
time.sleep(5)