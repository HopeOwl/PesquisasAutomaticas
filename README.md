from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

item = input('qual item? ')
pesquisa = str(f'{item} para que serve?' )

driver = webdriver.Chrome()
driver.get('https://www.google.com.br')
driver.find_element_by_name('q').send_keys(pesquisa + Keys.RETURN)
#driver.find_element_by_class_name('hgKElc').send_keys()

#1- Webscrapping
#2- automatização mesmo