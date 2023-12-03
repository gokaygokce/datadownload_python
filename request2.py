import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.petrolofisi.com.tr/akaryakit-fiyatlari')
#print(r.status_code)
#print(r.content)
#print(r.text)
soup = BeautifulSoup(r.content,"html.parser")
#yazdir = soup.find("p").text
yazdir = soup.find_all("p")
for i in yazdir:
    print(i.text)
#print(yazdir)
#print(soup.prettify())
#print(soup.title)