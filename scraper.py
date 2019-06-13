from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from parser import data_from_html_table
from utils import to_csv_file        

def go_index_page(page, perPage):
    driver.get(build_url(page))
    start =  2 if page == 0 else 3
    for i in range(perPage):
        driver.implicitly_wait(200)
        dataByRow = get_data_by_row(i+start,page)
        to_csv_file(dataByRow, 'data.csv') 
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
    html = soup.find('table')
    return data_from_html_table(html)


if __name__ == "__main__":
    pages = 3741
    perPage = 2
    pagesToTest = 3
    driver = webdriver.Firefox()  

    for page in range(pagesToTest):
        print('page', page)
        go_index_page(page, perPage)
    driver.quit()
    driver.close()


