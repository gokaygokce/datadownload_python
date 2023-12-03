import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.petrolofisi.com.tr/akaryakit-fiyatlari')
soup = BeautifulSoup(r.content,"html.parser")
yazdir = soup.find_all("ul", {"class":"list-group list-group-prices fs-6 fw-semibold d-lg-none"})
#print(yazdir)
for i in yazdir:
    print(i.text)
    