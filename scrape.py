import requests
import io
import os
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import traceback


years = [x for x in range(1989,2021,1)]
seasons = ['spring','fall']

brands  = set()


page = urlopen('https://www.vogue.com/fashion-shows/fall-2018-ready-to-wear')
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.findAll('a')


for x in name_box:
    try:
        post_split = x.get('href').split('/')
        if post_split[-2] == 'fall-2018-ready-to-wear':
            brands.add(post_split[-1])
    except:
        print(post_split,'does not work')


page = urlopen('https://www.vogue.com/fashion-shows/spring-2018-ready-to-wear')
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.findAll('a')


for x in name_box:
    try:
        post_split = x.get('href').split('/')
        if post_split[-2] == 'spring-2018-ready-to-wear':
            brands.add(post_split[-1])
    except:
        print(post_split,'does not work')


directory = os.fsencode(os.getcwd())

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".jpg"):
         if filename.split('_')[0] in brands:
            brands.remove(filename.split('_')[0])
            continue
     else:
         continue

print(len(brands))



for brand in brands:
    for year in years:
        for season in seasons:
            try:
                url = f'https://www.vogue.com/fashion-shows/{season}-{year}-ready-to-wear/{brand}/slideshow/collection/print'
                page = urlopen(url)
                soup = BeautifulSoup(page, 'html.parser')
                name_box = soup.find_all(attrs={'class': 'slide--image'})
                count = 1
                print(brand,year,season)
                for x in name_box:
                    img_url = x['src']
                    img_name = os.path.basename(img_url)
                    filename = f'{brand}_{year}_{season}_{count}.jpg'
                    fullfilename = os.path.join(os.getcwd(), filename)
                    urllib.request.urlretrieve(img_url, fullfilename)
                    count += 1



            except Exception:
                traceback.print_exc()

