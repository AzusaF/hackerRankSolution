# Calendar Module

import calendar
import datetime
date = list(map(int, input().split( )))
x = datetime.datetime(date[2], date[0], date[1])
print(x.strftime("%A").upper())
