from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
from utils import formatText

def table_to_json(table):
    rows = table.find_all('tr')
    data = []
    for row in rows[0:15]:
        cols = row.find_all('td')
        value = re.sub(' +', ' ',cols[1].text.strip())
        data.append(formatText(value))
        if(len(cols) == 4):
            data.append(cols[3].text.strip())
    data.append(rows[15].find('select').text.strip())
    return data
         

def go_index_page(page, perPage):
    driver.get(build_url(page))
   
    start =  2 if page == 0 else 3
    for i in range(perPage):
        driver.implicitly_wait(200)
        dataByRow = get_data_by_row(i+start,page)
        save_data_from_page(dataByRow) 
        driver.execute_script("window.history.go(-1)")
        

def build_url(page):
    return f'http://www.sunat.gob.pe/descarga/BueCont/BueCont{page}.html'

def get_data_by_row(index,page):
    elements = driver.find_elements_by_css_selector('a')
    try:
        row = elements[index]
    except IndexError:
        print(list(map( lambda x: x.text, elements)))
        print(index,page)
    row.click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "div_estrep")))
    return extract_data(driver.page_source)

def extract_data(source):
    soup = BeautifulSoup(source, 'html.parser')
    table = soup.find('table')
    return table_to_json(table)

def save_data_from_page(data):
    with open("data.csv", "a") as myfile:
        myfile.write(','.join(data) + '\n')


driver = webdriver.Firefox()   
pages = 3741
perPage = 2
pagesToTest = 3
f = open("data.csv","a") 

for page in range(pagesToTest):
    print('page', page)
    go_index_page(page, perPage)
driver.quit()
driver.close()
f.close()

