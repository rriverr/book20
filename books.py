


import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:yunayuna@cluster0.5i0os.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=2&orderClick=DAB&mallGb=KOR&linkClass=B',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
books = soup.select('#main_contents > ul > li')



for book in books :

    image = book.select_one('div.cover > a > img').get('src')
    title = book.select_one('div.detail > div.title > a > strong').get_text()
    info = book.select_one('div.detail > div.author').text.split('|')
    rank = book.select_one('div.detail > div.review > img').get('src')
    price = book.select_one('div.detail > div.price > strong').get_text()
    link = book.select_one('div.detail > div.title > a').get('href')
    author = info[0].strip()
    publisher = info[1].strip()
    pubday = info[2].strip()
    isbn = link[-13:]


    getsubPage = requests.get(link)
    subPage = BeautifulSoup(getsubPage.text, 'html.parser')


    getReviews = subPage.find("div", {"class":"box_detail_article"})
    # getReviews = subPage.select_one('#container > div:nth-child(7) > div.content_left > div:nth-child(5) > div:nth-child(25) > div:nth-child(2)')


    reviews = getReviews.text
    print(reviews)



    # doc = {
    #     'image':image,
    #     'title':title,
    #     'author':author,
    #     'publisher':publisher,
    #     'pubday':pubday,
    #     'rank':rank,
    #     'price':price,
    #     'link':link,
    #     'isbn':isbn
    # }
    # # db.books.insert_one(doc)

