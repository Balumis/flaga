# -*- coding: utf-8 -*-
from asyncore import write
import csv
import requests
from datetime import datetime
import re
from bs4 import BeautifulSoup
import sqlite3
from sys import argv

#https://www.youtube.com/watch?v=CEOTrWowqfo

xxxlutz = ['https://www.xxxlutz.at/tischplatten-C12C1C10C1',
            'https://www.xxxlutz.at/geschirrspueler-C41C3C6',
            'https://www.xxxlutz.at/tv-regale-tv-racks-C1C3C2',
            'https://www.xxxlutz.at/pfannensets-C65C1',
            'https://www.xxxlutz.at/bestecksets-C38C1?sort=popular&v_targetcolor=grau_silber',
            'https://www.xxxlutz.at/e-mobilitaet-C61C2C1',
            'https://www.xxxlutz.at/infrarotkabinen-C61C2C3C1',
            'https://www.xxxlutz.at/gartenschaukeln-C8C6']

url = 'https://www.xxxlutz.at/esstische-C12C1'
url_down1 = 'https://www.xxxlutz.at/p/linea-natura-esstisch-in-holz-200-100-75-cm-000898000101'
url_down2 = 'https://www.xxxlutz.at/p/wmf-universalzerkleinerer-0037311691'
url_down3 = 'https://www.xxxlutz.at/p/dieter-knoll-geschirrspueler-dkdt2901xk-000606000305'
url_down4 = 'https://www.bauhaus.info/tischplatten/pur-iternal-black-edition-tischplatte/p/27251250'
url_all = 'https://www.xxxlutz.at/geschirrspueler-C41C3C6'
url_tischplatten = 'https://www.xxxlutz.at/tischplatten-C12C1C10C1'
url_moebelix = 'https://www.moebelix.at/geschirrspueler-C8C4C4'

def clear_price(price):
    return price.replace('€', '').replace(',', '').replace('‒', '').replace('*', '').strip()

def get_conten_down_page(url):

    main_articel = []

    r = requests.get(url)
    r.encoding = r.apparent_encoding # decoding german chararter (üäö)
    page_source = r.text
    page_source = page_source.splitlines()

    for i in range(len(page_source)):
        if 'getContentPage' in str(page_source[i]):
            line_content = str(page_source[i]).split(',')

            start_index = '"locale":"de-AT"'
            #stop_index = '"summary":"'

            index_s = line_content.index(start_index)
            #index_x = line_content.index(stop_index)
            #print(index_s)
            #print(line_content[index_s])
            #print(index_x)
            #print(line_content[index_x])

            for l in range(index_s, index_s+100):
                #print(line_content[l])
                if 'description' in line_content[l]:
                    descritpion = line_content[l].split('"')
                    descritpion = descritpion[3].split('✓')
                    descritpion = descritpion[0]
                    #print(descritpion)
                    #print(1)
                    main_articel.append(descritpion)
                if 'currentPrice' in line_content[l]:
                    current_price = line_content[l+2].split(':')
                    current_price = current_price[1]
                    #print(current_price)
                    #print(2)
                    main_articel.append(current_price)
                if 'oldPrice' in line_content[l]:
                    old_price = line_content[l+1].split(':')
                    old_price = old_price[1].replace('}', '')
                    #print(old_price)
                #print(3)
                    main_articel.append(old_price)
                if 'canonicalUrl' in line_content[l]:
                    seo_url = line_content[l].split('"')
                    seo_url = seo_url[3]
                    #print(seo_url)
                    #print(4)
                    main_articel.append(seo_url)
                #print(line_content.index('url'))
                #print(page_source[i],'\n')
                with open('content_down_page.xml', "a", encoding='utf16') as f:
                    f.write(line_content[l])
                    f.write('\n')

    day_now = datetime.now().strftime('%Y-%m-%d')
    time_now = datetime.now().strftime('%H.%M.%S')
    main_articel.append(day_now)
    main_articel.append(time_now)

    with open('final_content_page.xml', "a", encoding='utf16') as f:
        f.write(str(main_articel) + '\n')
    print('OK')

#get_conten_down_page(url_down1)
#get_conten_down_page(url_down2)
#get_conten_down_page(url_down3)

#############################################################################################

def get_conten_main_page(url):

    #db = sqlite3.connect('dane.db')
    #cursor = db.cursor()

    if len(argv) > 1 and argv[1] == 'setup':
        cursor.execute('''CREATE TABLE offers (name TEXT, price REAL, price REAL)''')

    r = requests.get(url)
    r.encoding = r.apparent_encoding # decoding german chararter (üäö)
    page_source = r.text
    soup = BeautifulSoup(page_source, 'html.parser')

    for offer in soup.find_all('div', class_='_OEYzWglwj7E5gQdt'):
        title = offer.find('a').get_text()
        print(title)
        if offer.find('div', class_='_h9k2xhU7dZOy6yt8 _mjpXX8k3Z+QbXaVb'):
            current_price = clear_price(offer.find('div', class_='_h9k2xhU7dZOy6yt8').get_text())
            old_price = clear_price(offer.find('s').get_text())
            print(current_price)
            print(old_price)
        else:
            current_price = clear_price(offer.find('div', class_='_h9k2xhU7dZOy6yt8').get_text())
            print(current_price)
            print('Old price not avalaible')
        

get_conten_main_page(url_all)