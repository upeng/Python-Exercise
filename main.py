import time
a = "2019-5-10 20:40:00"
b=time.strptime(a,'%Y-%m-%d %H:%M:%S')
print(b.tm_year)

