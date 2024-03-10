import os
import requests
import parsing_lib as pars
from bs4 import BeautifulSoup

url = 'https://commons.wikimedia.org/wiki/List_of_dog_breeds'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Using CSS selector to find table
    table = soup.find('table', {'class': 'wikitable sortable'})

    names = []
    groups = []
    local_names = []
    dogpics = []

    for row in table.find_all('tr')[1:]:

        columns = row.find_all(['td', 'th'])

        name = columns[0].find('a').text.strip() # we need name.
        names.append(name)
        
        groups.append(columns[1].text.strip())
        
        span_tag = columns[2].find('span')
        local_names.append(span_tag.text.strip() if span_tag else '')

        img_tag = columns[3].find('img')
        pic = img_tag['src'] if img_tag else ''
        pars.download_image(pic, name)
        
    
        dogpics.append(pic)

print(names)

