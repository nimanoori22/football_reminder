from bs4 import BeautifulSoup as bs
import requests
from itertools import groupby
from collections import OrderedDict
import re
import json
import datetime

class Scraper:

    def __init__(self, site_url):
        self.site_url = site_url

    def page_catcher(self):
        with requests.session() as s:
            page = s.get(self.site_url)
            soup = bs(page.content, 'html.parser')
            return soup


class Select:

    def __init__(self, soup):
        self.soup = soup

    def live_table(self):
        mytb = []
        table = self.soup.find_all('div', class_='tv-schedule-box')
        for tbody in table:
            for t in tbody.findAll('tbody'):
                mytb.append(t)

        return mytb


    def date_selector(self):
        mylist = []
        table = self.soup.find_all('tr', class_='match-date')
        for th in table:
            for td in th.findAll('td'):
                mylist.append(td.text)
        return mylist

class Sorter:
    def __init__(self, table):
        self.table = table

    def split_by_date(self):
        mylist = []
        temp = '|'
        for item in self.table:
            if item.findAll('td', class_='sub-header'):
                mylist.append(temp)
                mylist.append(item)
            else:
                mylist.append(item)
        return mylist

    def list_splitor(self, mylist):
        return [list(g) for k, g in groupby(mylist, key=lambda x: x != "|") if k]

class Dictmaker:
    def __init__(self, items):
        self.items = items

    def maker(self):
        mydict = OrderedDict()
        temp = 0
        mydate = []
        for a in self.items:
            for item in a:
                try:
                    date = item.find('td', class_='sub-header')
                    if date:
                        d = item.find('td', class_='sub-header').text
                        mydate.append(d)
                        l = item.find_all('td', class_='text-center')[1].text
                        t = item.find('span', class_='match-time').text
                        n = item.find_all('td', class_='text-center')[2].text
                        c = item.find('span', class_='channel-name').text
                        c = " ".join(re.split("\s+", c, flags=re.UNICODE))
                        mydict[temp] = {'day':d, 'league':l, 'time':t, 'name':n, 'channel':c}
                        temp += 1 
                    else:
                        d = mydate[0]
                        l = item.find_all('td', class_='text-center')[0].text
                        t = item.find('span', class_='match-time').text
                        n = item.find_all('td', class_='text-center')[1].text
                        c = item.find('span', class_='channel-name').text
                        c = " ".join(re.split("\s+", c, flags=re.UNICODE))
                        mydict[temp] = {'day':d, 'league':l, 'time':t, 'name':n, 'channel':c}
                        temp += 1
                except IndexError:
                    pass
            mydate.clear()
        if not bool(mydict):
            return 'رویدادی در جدول پخش تلویزیون وجود ندارد'
        else:
            return mydict




