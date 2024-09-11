import calendar as cal

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

mon, day, year = map(int, input().split())

week_index = cal.weekday(year,mon,day)
print(weekdays[week_index].upper())


