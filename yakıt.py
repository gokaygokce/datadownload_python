import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.petrolofisi.com.tr/akaryakit-fiyatlari')
soup = BeautifulSoup(r.content, "html.parser")
for i in soup.find("ul", {"class": "list-group list-group-prices fs-6 fw-semibold d-lg-none"}).find_all("li"):
    sehir_Ad= i.find("li",{"class":"list-group-item p-3"})
    print(sehir_Ad)