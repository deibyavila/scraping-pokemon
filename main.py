import requests
from bs4 import BeautifulSoup
URL = 'https://pokemondb.net/pokedex/all'
URL_DETAIL = 'https://pokemondb.net/'
response = requests.get(URL)


if response.status_code == 200:
    print('nitido')
    
    soup = BeautifulSoup(response.text, 'html.parser')
    tag = soup.find_all(class_='ent-name')
    
    print(len(tag))
    for i in range(0,len(tag)):
        response_detail = requests.get(URL_DETAIL+tag[i].attrs['href'])
        soup_detail = BeautifulSoup(response_detail.text, 'html.parser')
        tag_2 = soup_detail.find('table', class_='vitals-table')
        data_tag_2 = tag_2.tbody.find_all('tr')        
        for td in data_tag_2[2].find_all('td'):
            species = td.text
        for td in data_tag_2[1].find_all('td'):
            types = td.text.replace('\n', ' ').strip()
             
        name = tag[i].attrs['href'].split('/')
        
        print('Name: ' + name[2] + ' Species: '+ species +' Types: '+ types)

else:
    print('algo salio mal')