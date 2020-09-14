
import requests
from bs4 import BeautifulSoup
import pandas


r = requests.get('https://tw.search.mall.yahoo.com/search/mall/product?p=dyson&qt=product&cid=hp&clv=0')
soup = BeautifulSoup(r.text,'lxml')


ary = []

for good in soup.select('.BaseGridItem__itemInfo___3E5Bx'):
    # print(good) # OK
    title = good.select_one('.BaseGridItem__title___2HWui').text
    price = good.select_one('.BaseGridItem__price___31jkj').text
    store = good.select_one('.StoreGridItem__storeName___2dutX').text
    # print(title, price, store)
    ary.append({'title':title, 'price':price, 'store':store})
    # print('======================')

df = pandas.DataFrame(ary)
print(df.head()) #只取前面五項