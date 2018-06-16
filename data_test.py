"""year = 2018
#month = 6
#day = 12

day_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year % 100 != 0 and year % 4 == 0:
    print('rok przestępny')
elif year % 100 == 0 and year % 400 != 0:
    print('rok nie jest przestępny')


day_in_month[i-1]"""

day_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day=1
month=6
year=2018


if day <= day_in_month[month-1]:
    day=+1
else:
    day = 1
if month <= len(day_in_month):
    month = 1
else:
    month = month
print(day,'-',month,'-',year)