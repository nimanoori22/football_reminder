import jdatetime
from persiantools.jdatetime import JalaliDateTime

class TimeManage:

    def __init__(self, dateStr, hourStr):
        self.dateStr = dateStr
        self.hourStr = hourStr

    @property
    def yearChoose(self):

        date = self.dateStr.split(' ')
        if jdatetime.datetime.now().month != 12:
            return jdatetime.datetime.now().year
        
        else:
            if date[2] != 'فروردین':
                return jdatetime.datetime.now().year
            else:
                return  jdatetime.datetime.now().year + 1

    @property
    def month(self):

        months = {
            
            'فروردین': 1,
            'اردیبهشت': 2,
            'خرداد': 3,
            'تیر': 4,
            'مرداد': 5,
            'شهریور': 6,
            'مهر': 7,
            'آبان': 8,
            'آذر': 9,
            'دی': 10,
            'بهمن': 11,
            'اسفند': 12,
        }
        return months

    def timeObjMaker(self, time_str):
        """
        returns jalali datetime objects
        """
        date_time_obj = jdatetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M')
        return date_time_obj

    @property
    def timeExtractor(self):

        date = self.dateStr.split(' ')
        del date[0]
        for key, value in self.month.items():
            if key in  date:
                date[1] = value
        
        hour = self.hourStr.split(' ')[1]
        time_str_start = f'{self.yearChoose}-{date[1]}-{date[0]} {hour}'

        return time_str_start


    def match_start_end(self):
        start_time = self.timeObjMaker(self.timeExtractor)
        end_time = start_time + jdatetime.timedelta(hours=2)
        return [start_time, end_time]
    
    def gregorian_start_end(self):
        times = self.match_start_end() 
        return [JalaliDateTime(item.year, item.month, item.day, item.hour, item.minute).to_gregorian() for item in times]

