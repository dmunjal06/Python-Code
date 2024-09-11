def check_leapYear(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("this year is a leap year")
    else:
        print("not a leap year")

check_leapYear(2001)
