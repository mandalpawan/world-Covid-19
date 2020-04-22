import requests 
from bs4 import BeautifulSoup
from csv import writer
from datetime import date

today = date.today()


def get_corona_data():
    url="https://www.worldometers.info/coronavirus/"
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    gdp_table = soup.find("table", id = "main_table_countries_today")
    gdp_table_data = gdp_table.tbody.find_all("tr")

    # Getting all countries names
    dicts = {}
    for i in range(len(gdp_table_data)):
        try:
            key = (gdp_table_data[i].find_all('a', href=True)[0].string)
        except:
            key = (gdp_table_data[i].find_all('td')[0].string)

        value = [j.string for j in gdp_table_data[i].find_all('td')]
        dicts[key] = value
    return dicts

data = get_corona_data()
upload_list = []
header_list = ['country', 'total_case', 'new_cases', 'total_death', 'new_death', 'total_recovery', 'active_cases', 'serious_critical', 'total_case_perM', 'totalDeathperM', 'total_test_perM', 'test_perM', 'continent']
upload_list.append(header_list)
for item in data:
    upload_list.append((data[item]))
file_name = 'data'+str(today)+'.csv'
with open(file_name ,'w',newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerows(upload_list)