import pandas as pd
from bs4 import BeautifulSoup
with open("data.html","r") as f:
    content = f.read()
    soup = BeautifulSoup(content,"html.parser")
    link = soup.find_all(class_ = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    name_list = []
    price_list = []
    rating_list = []
    for name in link:
        name_list.append(name.get('href').split('/')[1])
    link = soup.find_all(class_ = "a-row a-size-small")
    for rating in link:
        rating_list.append(rating.span['aria-label'][:3])
    link = soup.find_all(class_ = "a-offscreen")
    for price in link:
        # print(price.text[3:])
        price_list.append(price.text[3:])
    print(name_list[0])
    df = pd.DataFrame({"Name":name_list[:11],"Price":price_list[:11],"Rating":rating_list[:11]})
    blankIndex=[''] * len(df)
    df.index=blankIndex
    print(df)