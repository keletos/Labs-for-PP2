import datetime

x = datetime.datetime.now()
print(x.replace(microsecond=0))

#


def Diff(a,b):
    return (a-b).total_seconds()

#


date_now = datetime.datetime.now()
new_date = date_now - datetime.timedelta(days=5)

print(new_date)

#

print(datetime.datetime.today())
print(datetime.datetime.today() + datetime.timedelta(days=1))
print(datetime.datetime.today() - datetime.timedelta(days=1))