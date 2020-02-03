"""Get a time at a proportion of a range of two formatted times.

To change time frame, replace strings in strtimes and endtimes. 
"""

import random
import time

def str_time_prop(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%I:%M %p', prop)

strtimes = ["9:00 AM", "12:00 PM", "3:00 PM", "6:00 PM"]
endtimes = ["12:00 PM", "3:00 PM", "6:00 PM", "9:00 PM"]

for (strtime, endtime) in zip(strtimes, endtimes):
    print(random_date(strtime, endtime, random.random()))
