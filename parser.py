import re
from utils import formatText

def data_from_html_table(table):
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