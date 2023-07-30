import datetime
now = datetime.datetime.now()

print(now.strftime("%d:%m:%Y"))

print(datetime.date.today())


x = datetime.datetime(2020,11,10)
print(x)

y = datetime.datetime(2019,11,10)
print(y)
diff = x-y
print(diff)


end =datetime.datetime.now()

difference = end - now
print(difference)