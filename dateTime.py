# in this program i will try to cover all datetime method 
import datetime as dt
# know for today date
today=dt.date.today()
print('this is my current date',today)
print()
# know for the time
time2=dt.datetime.now()
print('this is my curent time and date ',time2)
# output 2021-07-07 20:52:12.978336
print(time2)
print(time2.year)
print(time2.month)
print(time2.day)
print(time2.hour)
print(time2.minute)
print(time2.second)
print(time2.microsecond)



# ,,,,,,,,,,,,and we want to provide own time and date,,,,,,,,,
dat=dt.date(year=2000,month=3,day=14)
print(f"this is my date of birth {dat.day,dat.month,dat.year}")

# ,,,,,,,,,,,,and we want to provide date in another type,,,,,,,,,,,,,,
datee=dt.date(2000,3,14)
print(datee)
print(datee.year)
print(datee.month)
print(datee.day)
print()

# ,,,,,,,,,,,,we want provide alse time in this programe,,,,,,,,,,

timee=dt.time(hour = 12,minute = 30,second = 12)
print('\n')
print(f"this is my provided time {timee}")
print('this is hour',timee.hour)
print("this is minute",timee.minute)
print("this is second",timee.second)
print("this is microdsecond",timee.microsecond,"\n")
print("mohit","\t","ranjit","\\",'\n')
timeee=dt.time(10,2,3)
print(timeee)
print(f"this is my provided time {timeee}")
print('this is hour',timeee.hour)
print("this is minute",timeee.minute)
print("this is second",timeee.second)
print("this is microdsecond",timeee.microsecond,"\n")


# ,,,,,,,,,and now we are using datetime function in datetime class,,,,,,,,,]]
datandtime=dt.datetime(year=2000,month=12,day=13,hour=8,minute=34,second=23,microsecond=23342)
print(datandtime,'\n')
print(datandtime.year)
print(datandtime.month)
print(datandtime.day)
print(datandtime.hour)
print(datandtime.minute)
print(datandtime.second)
print(datandtime.microsecond)


# ,,,,,,,,,,and here another method on the datetime function,,,,,,,,,,
drr=dt.datetime.now()
print("this is current date and time", drr)
print()
print(drr.year)
print(drr.month)
print(drr.day)
print(drr.hour)
print(drr.minute)
print(drr.second)

# print(drr.day)
# drrr=dt.datetime.year
# print(drrr)
# print(dr)
# print(dt.datetime.hour())
# print(dt.datetime.minute())
# print(dt.datetime.second())

# ,,,,,,timedelta concept,,,,,,,,,,,,
# in this concept, we compare two time table
# ,,,question what is the date after two year as to current date
current_date_time=dt.datetime.now()
print(current_date_time)
futur_date_after_two_year =current_date_time + dt.timedelta(days=730)
print("future date after two year",futur_date_after_two_year)
print(futur_date_after_two_year.hour)
print(futur_date_after_two_year.minute)
print(futur_date_after_two_year.second,"\n")
print(f"future date {futur_date_after_two_year.day} ")
print(futur_date_after_two_year.day)
print(futur_date_after_two_year.month)
print(futur_date_after_two_year.year)



