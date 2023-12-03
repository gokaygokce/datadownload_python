import requests
r = requests.get('https://www.petrolofisi.com.tr/akaryakit-fiyatlari')
print(r.status_code)
#print(r.content)
print(r.text)