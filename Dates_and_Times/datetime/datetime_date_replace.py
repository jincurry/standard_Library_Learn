import datetime


d1 = datetime.date(2018, 3, 8)
print('d1:', d1.ctime())

d2 = d1.replace(2018, 3, 9)
print('d2:', d2.ctime())
