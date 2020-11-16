import datetime

myDay = input("please enter the day you were born: ")
myMonth = input("please enter the month you were born: ")
myYear = input("please enter the year you were born: ")

print ("your birthday is on "+str(myYear)+" "+str(myMonth)+" "+str(myDay))

myBirthday = datetime.date(int (myYear), int(myMonth), int(myDay))
today = datetime.date.today()
dayDiff = (today-myBirthday)

print ("Your age is "+str(int(dayDiff.days/365.25))+" Years")
