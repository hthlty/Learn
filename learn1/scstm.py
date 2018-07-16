#coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.scstm.com/')

driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li[1]/a/div[2]/h3').click()

data = driver.page_source()