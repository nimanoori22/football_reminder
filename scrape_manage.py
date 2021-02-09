import json
from scraper.match_scraper import (
    Scraper,
    Select, 
    Sorter, 
    Dictmaker
)

from football_reminder import db
from football_reminder.time_manage import TimeManage
from utilities.utility import getFromdb

from football_reminder.models import Match


myscraper = Scraper('https://www.varzesh3.com/')
soup = myscraper.page_catcher()

myselector = Select(soup)

table = myselector.live_table()
mysorter = Sorter(table)
mylist = mysorter.split_by_date()

items = mysorter.list_splitor(mylist)

mymake = Dictmaker(items)

mydict = mymake.maker()


ss = mydict
names = getFromdb(Match, 'teams')

for key, value in ss.items():
    if value['name'] in names:
        continue
    else:
        matchTime = TimeManage(value['day'], value['time'])
        startandend = matchTime.gregorian_start_end()
        game = Match(
            teams = value['name'],
            day = value['day'],
            match_datetime_start = startandend[0],
            match_datetime_end = startandend[1],
            channel = value['channel'],
            league = value['league'],
            time = value['time']
        )
        db.session.add(game)
db.session.commit()