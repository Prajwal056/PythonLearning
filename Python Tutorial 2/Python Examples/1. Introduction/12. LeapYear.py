
def Leap_year(year):
    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
        print("%d is a Leap year" %year)
    else:
        print("%d is Not" %year)

Leap_year(2000)