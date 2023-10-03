        
import datetime

# Get the current date
current_date = datetime.date.today()

# Format the current date as a string
today_date = current_date.strftime("%d-%m-%Y")


            #taking dates input
date1 = input("Enter your date of birth(dd-mm-yyyy):")
date2 = today_date

dd1 = date1[0:2]        #day of first date
dd1 = int(dd1)

dd2 = date2[0:2]        #day of second date
dd2 = int(dd2)


mm1 = date1[3:5]        #month of first date
mm1 = int(mm1)
mm2 = date2[3:5]        #month of second date
mm2 = int(mm2)

yyyy1 = date1[6:10]     #year of first date
yyyy1 = int(yyyy1)
yyyy2 = date2[6:10]     #year of second date
yyyy2 = int(yyyy2)

if(yyyy2<yyyy1):
    print("please enter a valid date")
else:
    if dd2 < dd1:
        dd2 += 30
        day = dd2-dd1
        mm1 += 1
    else:
        day = dd2-dd1

    if mm2<mm1:
        mm2 += 12
        month = mm2-mm1
        yyyy1 += 1
    else:
        month = mm2-mm1
    year = yyyy2 - yyyy1
    print("Difference between dates is:",day,"days",month,"months",year,"year")

    total_day = day + (month*30) + (year*365)
    total_month = total_day // 30
    total_year = total_month // 12
    total_hour = total_day*24
    total_minite = total_hour*60
    total_second = total_minite*60

    print("you are",total_day,"days old as of today")
    print("you are",total_month,"months old as of today")
    print("you are",total_year,"years old as of today")
    print("you are",total_hour,"hours old as of today")
    print("you are",total_minite,"minites old as of today")
    print("you are",total_second,"seconds old as of today")