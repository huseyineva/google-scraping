import requests
from bs4 import BeautifulSoup

search_input = input('Aramak istediginiz kelimeyi giriniz: ').replace(' ','+')
link = "https://www.google.com/search?q=" + search_input

header_params = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}
response = requests.get(link, headers = header_params)

soup = BeautifulSoup(response.content, "html.parser")

results = soup.find_all('div', class_="jtfYYd")

for div in results:
    anchor = div.find('a')

    link = anchor['href']
    text = anchor.find('h3').string
    

    print(link + '\n' + text)
    print('--------------------------------------')
