import requests 
from bs4 import BeautifulSoup

'''
#Url = "https://www.covid19india.org/"
def get_corona_data(url):
    return requests.get(url).text


Url ="https://www.worldometers.info/coronavirus/"
r = get_corona_data(Url)
soup = BeautifulSoup(r,'html.parser')

#print(soup.prettify()) 
mystr = ""
for table in soup.find_all('tbody')[0].find_all('tr'):
    mystr += table.get_text()

itemlist = mystr.split("\n\n")   

for item in itemlist:
    print(item.split("\n"))'''
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
region = []
confirmed = []
deceased = []
recovered = []
serious = []
details = []

for i in data:
    region.append(data[i][0])
    confirmed.append(str(data[i][1]))
    deceased.append(data[i][3])
    recovered.append(data[i][5])
    serious.append(data[i][7])

val = []
result = []
for j in deceased:
    if(j.isspace()):
        result.append('None')
    else:
        result.append(j)

for value in confirmed:
    val.append(value.replace(',',''))
    
confirmed = confirmed[2:]

print(confirmed)




