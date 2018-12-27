#!/usr/bin/env python

from selenium import webdriver
import time

url = "https://www.baidu.com"
dr = webdriver.Firefox()
dr.get(url)
dr.find_element_by_name("wd").send_keys("Python Selenium")
dr.find_element_by_id('su').click()
time.sleep(5)
dr.quit()