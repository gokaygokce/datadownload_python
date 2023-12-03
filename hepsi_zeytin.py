import requests
from bs4 import BeautifulSoup

url = requests.get(
    "https://www.akakce.com/sivi-yag/kristal-zeytinyagi.html?gad_source=1&gclid=Cj0KCQiA67CrBhC1ARIsACKAa8R04elWyTEGKHfrMp0j9_n3V1PRmoa9IU9rvUkkCwS8GEKy-N-ybXEaAnWYEALw_wcB")
print(url.status_code)
soup = BeautifulSoup(url.content, "html.parser")
sayı =1
for i in soup.find("ul", {"class": "pl_v9 qv_v9"}).find_all("li"):
    isim_al = i.find("h3", {"class": "pn_v8"}).text
    fiyat_al = i.find("span", {"class": "pt_v9"}).text.strip()
    link = i.find("a",{"class": "iC"}).get("href")
    print("*"*40)
    print(f"{sayı} :Zeytin Yağı Adı:{isim_al}\nFiyatı: {fiyat_al}\nlink : {link}")
    sayı+=1
    print("*" * 40)