from bs4 import BeautifulSoup
import requests
url = "https://www.amazon.in/s?k=headphones&ref=nb_sb_noss_2"
r = requests.get(url,auth=('user', 'pass'))
print(r.text)
with open("data.html","w",encoding="utf-8") as f:
    f.write(r.text)