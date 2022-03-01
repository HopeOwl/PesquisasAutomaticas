from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

item = input('qual item? ')
pesquisa = str(f'{item} para que serve?' )

driver = webdriver.Chrome()
driver.get('https://www.google.com.br')
driver.find_element(By.NAME, 'q').send_keys(pesquisa + Keys.RETURN)
