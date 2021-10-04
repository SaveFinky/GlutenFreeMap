from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

regione = input('Inserisci la regione: ')

provincia = input('Inserisci la provincia: ')

comune = input('Inserisci il comune: ')

web = webdriver.Chrome()
web.get('http://www.ristorantiperceliaci.net/')

time.sleep(2)

regSelect = Select(web.find_element_by_xpath('/html/body/div/div/div[3]/div[4]/div[1]/select[1]'))
regSelect.select_by_visible_text(regione)
time.sleep(1)

provSelect = Select(web.find_element_by_xpath('/html/body/div/div/div[3]/div[4]/div[1]/select[2]'))
provSelect.select_by_visible_text(provincia)
time.sleep(1)

comSelect = Select(web.find_element_by_xpath('/html/body/div/div/div[3]/div[4]/div[1]/select[3]'))
comSelect.select_by_visible_text(comune)
time.sleep(1)

Submit = web.find_element_by_xpath('/html/body/div/div/div[3]/div[4]/div[1]/form/input[4]')
Submit.click()

time.sleep(3)

for tag in web.find_elements_by_class_name('nome'):
    print(tag.get_attribute("title"))



 #/html/body/div/div/div[3]/div[2]/table[3]/tbody/tr/td[1]/span/a
 #/html/body/div/div/div[3]/div[2]/table[4]/tbody/tr/td[1]/span/a
 #/html/body/div/div/div[3]/div[2]/table[5]/tbody/tr/td[1]/span/a
 #/html/body/div/div/div[3]/div[2]/table[6]/tbody/tr/td[1]/span/a
 #web.execute_script("window.open('https://www.google.it/maps', 'new_window')") 

