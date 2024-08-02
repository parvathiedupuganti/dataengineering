year = int(input("Enter the year : "));
#print(type(year))
"""
if(year%400 == 0):
    print(year, "is leap year")

else:
    if (year%100!=0):
        if(year %4==0):
            print(year, "is leap year")
        else:
            print(year, "is not leap year")
    else:
        print(year, "is not leap year")
"""
"""
if(year%400==0):
    print(year, "is leap year")
elif (year%100!=0 and year%4==0):
    print(year, "is leap year")
else:
    print(year, "is not leap year")

"""

if (year%400==0 or (year%100!=0 and year%4==0)):
    print(year, "is leap year")
else:
    print(year, "is not leap year")
    


