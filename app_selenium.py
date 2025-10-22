import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = 'https://books.toscrape.com/'

# A classe Service é usada para iniciar uma instancia do chrome webdriver.
service = Service()

# webdriver.ChromeOptions é usado para definir a preferencia para o brower do chrome.
options = webdriver.ChromeOptions()

# Inicia-se a intancia do Chome webdriver com as definidas 'options' e 'service'.
driver = webdriver.Chrome(service=service, options=options)

#chama a URL.
driver.get(url)

# Como Encontrar Elementos do HTML
# - find_element(By.ID,"id")
# - find_element(By.NAME,"name")
# - find_element(By.XPATH,"xpath")
# - find_element(By.LINK_TEXT,"link text")
# - find_element(By.PARTIAL_LINK_TEXT,"partial link text")
# - find_element(By.TAG_NAME,"tag name")
# - find_element(By.CLASS_NAME,"class name")
# - find_element(By.CSS_SELECTOR, "css selector")


# Pegando o/os elemento/s

# driver.find_element(By.TAG_NAME,'a').text -> um elemento
#driver.find_elements(By.TAG_NAME,'a')[54].text -> pega o elemento especifico
driver.find_elements(By.TAG_NAME,'a')[54].get_attribute('title')

#Salvando a lista de titulos em um variavel
title_elements = driver.find_elements(By.TAG_NAME,'a')[54:94:2]

list_storage =[]
for key in range(len(title_elements)):
    title_elements[key].click()
    values = int(driver.find_element(By.CLASS_NAME,"instock").text.replace('In stock (','').replace(' available)','')) #class="instock availability" não pode ter espaço
    list_storage.append(values)
    driver.back()

#listas com os titulos

list_titles = [title.get_attribute('title') for title in title_elements]

dect_df = {"TITLE":list_titles, "QTD_STOCK":list_storage}
df = pd.DataFrame(dect_df)
