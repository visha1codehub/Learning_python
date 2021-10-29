import datetime
import pytz
db = datetime.date(2022,1,4)
vb = datetime.date(2022,3,10)
print(db)

curr_time = datetime.datetime.now().time()
print(curr_time)

tday  = datetime.date.today()
print(tday)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday+tdelta)
print(tday-tdelta)

bday_diff = vb - db
print(bday_diff.total_seconds())

dt_utc = datetime.datetime.now(tz=pytz.UTC)
print(dt_utc)

dt_mnt = dt_utc.astimezone(pytz.timezone('Asia/Kolkata'))

